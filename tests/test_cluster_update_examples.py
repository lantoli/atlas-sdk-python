import os
import sys
from types import SimpleNamespace

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "examples"))

from pause_cluster import wait_for_cluster_state
from scale_cluster import replication_specs_with_instance_size
from disk_usage import (
    DiskUsage,
    cluster_processes,
    configured_disk_line,
    disk_size_gb,
    latest_disk_values,
)
from update_autoscaling import parse_bool, replication_specs_with_auto_scaling
import update_autoscaling
from provision_big_cluster import build_replication_specs
from mongodb_atlas import (
    AdvancedAutoScalingSettings,
    CloudRegionConfig20240805,
    DedicatedHardwareSpec20240805,
    HardwareSpec20240805,
    ReplicationSpec20240805,
)


def test_wait_for_cluster_state_polls_until_target_state():
    states = iter(["UPDATING", "IDLE"])
    calls = []

    class FakeClusters:
        def get_cluster(self, group_id, cluster_name):
            calls.append((group_id, cluster_name))
            return SimpleNamespace(state_name=next(states))

    result = wait_for_cluster_state(
        client=SimpleNamespace(clusters=FakeClusters()),
        project_id="project-id",
        cluster_name="cluster-name",
        target_state="IDLE",
        timeout_seconds=10,
        poll_seconds=0,
        sleep=lambda _: None,
    )

    assert result.state_name == "IDLE"
    assert calls == [("project-id", "cluster-name"), ("project-id", "cluster-name")]


def test_wait_for_cluster_state_times_out():
    class FakeClusters:
        def get_cluster(self, group_id, cluster_name):
            return SimpleNamespace(state_name="UPDATING")

    with pytest.raises(TimeoutError):
        wait_for_cluster_state(
            client=SimpleNamespace(clusters=FakeClusters()),
            project_id="project-id",
            cluster_name="cluster-name",
            target_state="IDLE",
            timeout_seconds=0,
            poll_seconds=0,
            sleep=lambda _: None,
        )


def test_replication_specs_with_instance_size_updates_all_node_types():
    specs = [
        ReplicationSpec20240805(
            region_configs=[
                CloudRegionConfig20240805(
                    electable_specs=HardwareSpec20240805(instance_size="M10", node_count=3),
                    read_only_specs=DedicatedHardwareSpec20240805(instance_size="M10", node_count=1),
                    analytics_specs=DedicatedHardwareSpec20240805(instance_size="M10", node_count=1),
                )
            ]
        )
    ]

    updated = replication_specs_with_instance_size(specs, "M20")
    region = updated[0].region_configs[0]

    assert region.electable_specs.instance_size == "M20"
    assert region.read_only_specs.instance_size == "M20"
    assert region.analytics_specs.instance_size == "M20"
    assert specs[0].region_configs[0].electable_specs.instance_size == "M10"


def test_disk_usage_filters_processes_for_cluster_name():
    processes = [
        SimpleNamespace(id="cluster-a-shard-00-00.example.mongodb.net:27017", hostname=None),
        SimpleNamespace(id="other-shard-00-00.example.mongodb.net:27017", hostname=None),
        SimpleNamespace(id=None, hostname="cluster-a-shard-00-01.example.mongodb.net"),
    ]

    matched = cluster_processes(processes, "Cluster-A")

    assert [process.id or process.hostname for process in matched] == [
        "cluster-a-shard-00-00.example.mongodb.net:27017",
        "cluster-a-shard-00-01.example.mongodb.net",
    ]


def test_disk_usage_reads_configured_and_used_sizes():
    cluster = SimpleNamespace(
        replication_specs=[
            ReplicationSpec20240805(
                region_configs=[
                    CloudRegionConfig20240805(
                        electable_specs=HardwareSpec20240805(
                            instance_size="M10",
                            disk_size_gb=40.0,
                            node_count=3,
                        )
                    )
                ]
            )
        ]
    )
    measurements = SimpleNamespace(
        measurements=[
            SimpleNamespace(
                name="DISK_PARTITION_SPACE_USED",
                data_points=[
                    SimpleNamespace(value=None),
                    SimpleNamespace(value=10 * 1024**3),
                ],
            ),
            SimpleNamespace(
                name="DISK_PARTITION_SPACE_FREE",
                data_points=[SimpleNamespace(value=30 * 1024**3)],
            ),
        ]
    )

    assert disk_size_gb(cluster) == 40.0
    assert latest_disk_values(measurements) == {
        "DISK_PARTITION_SPACE_USED": 10 * 1024**3,
        "DISK_PARTITION_SPACE_FREE": 30 * 1024**3,
    }


def test_disk_usage_summary_includes_most_used_disk():
    line = configured_disk_line(
        64.0,
        [
            DiskUsage("host-a:27017", "data", used_bytes=6 * 1024**3, free_bytes=58 * 1024**3),
            DiskUsage("host-b:27017", "data", used_bytes=8 * 1024**3, free_bytes=56 * 1024**3),
            DiskUsage("host-c:27017", "data", used_bytes=None, free_bytes=None),
        ],
    )

    assert line == "Configured disk size: 64.0 GB. Most used disk: host-b:27017 (data), 8.0 GB used, 12.5%."


def test_replication_specs_with_auto_scaling_updates_region_settings():
    specs = [
        ReplicationSpec20240805(
            region_configs=[CloudRegionConfig20240805(electable_specs=HardwareSpec20240805(node_count=3))]
        )
    ]

    updated = replication_specs_with_auto_scaling(
        specs,
        enabled=True,
        min_instance_size="M10",
        max_instance_size="M30",
        scale_down_enabled=True,
        disk_enabled=True,
    )
    auto_scaling = updated[0].region_configs[0].auto_scaling

    assert isinstance(auto_scaling, AdvancedAutoScalingSettings)
    assert auto_scaling.compute.enabled is True
    assert auto_scaling.compute.min_instance_size == "M10"
    assert auto_scaling.compute.max_instance_size == "M30"
    assert auto_scaling.compute.scale_down_enabled is True
    assert auto_scaling.disk_gb.enabled is True


def test_parse_bool_accepts_common_values():
    assert parse_bool("true") is True
    assert parse_bool("1") is True
    assert parse_bool("false") is False
    assert parse_bool("0") is False


def test_update_autoscaling_waits_until_cluster_is_idle(monkeypatch):
    waited = []
    updated_specs = []

    class FakeClusters:
        def get_cluster(self, group_id, cluster_name):
            return SimpleNamespace(
                replication_specs=[
                    ReplicationSpec20240805(
                        region_configs=[
                            CloudRegionConfig20240805(
                                electable_specs=HardwareSpec20240805(node_count=3)
                            )
                        ]
                    )
                ]
            )

        def update_cluster(self, **kwargs):
            updated_specs.extend(kwargs["replication_specs"])
            return SimpleNamespace(name=kwargs["cluster_name"])

    def fake_wait_for_cluster_state(**kwargs):
        waited.append(kwargs)

    monkeypatch.setenv("MONGODB_ATLAS_PROJECT_ID", "project-id")
    monkeypatch.setenv("MONGODB_ATLAS_CLUSTER_NAME", "cluster-name")
    monkeypatch.setenv("MONGODB_ATLAS_AUTOSCALING_ENABLED", "true")
    monkeypatch.setenv("MONGODB_ATLAS_AUTOSCALING_MIN_INSTANCE_SIZE", "M10")
    monkeypatch.setenv("MONGODB_ATLAS_AUTOSCALING_MAX_INSTANCE_SIZE", "M30")
    monkeypatch.setattr(
        update_autoscaling,
        "get_client",
        lambda: SimpleNamespace(clusters=FakeClusters()),
    )
    monkeypatch.setattr(update_autoscaling, "wait_for_cluster_state", fake_wait_for_cluster_state)

    update_autoscaling.main()

    assert updated_specs
    assert waited
    assert waited[0]["project_id"] == "project-id"
    assert waited[0]["cluster_name"] == "cluster-name"
    assert waited[0]["target_state"] == "IDLE"


def test_big_cluster_replication_specs_match_terraform_shape():
    specs = build_replication_specs()

    assert len(specs) == 4
    assert [spec.zone_name for spec in specs] == ["zone n1", "zone n1", "zone n2", "zone n2"]

    for spec in specs[:2]:
        assert len(spec.region_configs) == 2
        aws, azure = spec.region_configs
        assert aws.provider_name == "AWS"
        assert aws.region_name == "US_WEST_2"
        assert aws.priority == 7
        assert aws.electable_specs.instance_size == "M10"
        assert aws.electable_specs.node_count == 3
        assert azure.provider_name == "AZURE"
        assert azure.region_name == "US_EAST_2"
        assert azure.priority == 6
        assert azure.electable_specs.instance_size == "M10"
        assert azure.electable_specs.node_count == 2

    for spec in specs[2:]:
        assert len(spec.region_configs) == 2
        aws, azure = spec.region_configs
        assert aws.provider_name == "AWS"
        assert aws.region_name == "EU_WEST_1"
        assert aws.priority == 7
        assert azure.provider_name == "AZURE"
        assert azure.region_name == "EUROPE_NORTH"
        assert azure.priority == 6
