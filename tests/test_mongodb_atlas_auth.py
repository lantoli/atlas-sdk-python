import os
import sys

import httpx
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from mongodb_atlas import (
    AtlasClient,
    CloudRegionConfig20240805,
    ClusterManager,
    DedicatedHardwareSpec20240805,
    HardwareSpec20240805,
    ReplicationSpec20240805,
)


class FakeResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return {"access_token": "test-token"}


def test_from_service_account_fetches_token_and_builds_client(monkeypatch):
    calls = []

    def fake_post(url, *, data, auth):
        calls.append((url, data, auth))
        return FakeResponse()

    monkeypatch.setattr(httpx, "post", fake_post)

    client = AtlasClient.from_service_account(
        client_id="client-id",
        client_secret="client-secret",
        base_url="https://cloud-dev.mongodb.com",
    )

    assert calls == [
        (
            "https://cloud-dev.mongodb.com/api/oauth/token",
            {"grant_type": "client_credentials"},
            ("client-id", "client-secret"),
        )
    ]
    assert client._client_wrapper._base_url == "https://cloud-dev.mongodb.com"
    assert client._client_wrapper._token == "test-token"
    assert client._client_wrapper.get_custom_headers() == {
        "Accept": "application/vnd.atlas.2025-03-12+json"
    }


def test_from_env_reads_service_account_environment(monkeypatch):
    monkeypatch.setenv("MONGODB_ATLAS_CLIENT_ID", "env-client-id")
    monkeypatch.setenv("MONGODB_ATLAS_CLIENT_SECRET", "env-client-secret")
    monkeypatch.setenv("MONGODB_ATLAS_BASE_URL", "https://cloud-dev.mongodb.com")

    def fake_post(url, *, data, auth):
        assert auth == ("env-client-id", "env-client-secret")
        return FakeResponse()

    monkeypatch.setattr(httpx, "post", fake_post)

    client = AtlasClient.from_env()

    assert client._client_wrapper._base_url == "https://cloud-dev.mongodb.com"
    assert client._client_wrapper._token == "test-token"


def test_from_env_reports_missing_credentials(monkeypatch):
    monkeypatch.delenv("MONGODB_ATLAS_CLIENT_ID", raising=False)
    monkeypatch.delenv("MONGODB_ATLAS_CLIENT_SECRET", raising=False)

    with pytest.raises(RuntimeError, match="MONGODB_ATLAS_CLIENT_ID"):
        AtlasClient.from_env()


def test_from_service_account_merges_custom_headers(monkeypatch):
    def fake_post(url, *, data, auth):
        return FakeResponse()

    monkeypatch.setattr(httpx, "post", fake_post)

    client = AtlasClient.from_service_account(
        client_id="client-id",
        client_secret="client-secret",
        headers={"X-Test": "1"},
    )

    assert client._client_wrapper.get_custom_headers() == {
        "Accept": "application/vnd.atlas.2025-03-12+json",
        "X-Test": "1",
    }


def test_versioned_content_type_sets_matching_accept(monkeypatch):
    captured_headers = {}

    def fake_httpx_request(method, url, *, headers, **kwargs):
        captured_headers.update(headers)
        return httpx.Response(200, json={})

    monkeypatch.setattr(httpx, "post", lambda url, *, data, auth: FakeResponse())
    client = AtlasClient.from_service_account(
        client_id="client-id",
        client_secret="client-secret",
    )
    monkeypatch.setattr(
        client._client_wrapper.httpx_client.httpx_client,
        "request",
        fake_httpx_request,
    )

    client._client_wrapper.httpx_client.request(
        "api/atlas/v2/groups/group-id/clusters",
        method="POST",
        headers={"content-type": "application/vnd.atlas.2024-10-23+json"},
    )

    assert captured_headers["Accept"] == "application/vnd.atlas.2024-10-23+json"


def test_explicit_accept_request_option_is_preserved(monkeypatch):
    captured_headers = {}

    def fake_httpx_request(method, url, *, headers, **kwargs):
        captured_headers.update(headers)
        return httpx.Response(200, json={})

    monkeypatch.setattr(httpx, "post", lambda url, *, data, auth: FakeResponse())
    client = AtlasClient.from_service_account(
        client_id="client-id",
        client_secret="client-secret",
    )
    monkeypatch.setattr(
        client._client_wrapper.httpx_client.httpx_client,
        "request",
        fake_httpx_request,
    )

    client._client_wrapper.httpx_client.request(
        "api/atlas/v2/groups/group-id/clusters",
        method="POST",
        headers={"content-type": "application/vnd.atlas.2024-10-23+json"},
        request_options={
            "additional_headers": {"Accept": "application/vnd.atlas.2023-01-01+json"}
        },
    )

    assert captured_headers["Accept"] == "application/vnd.atlas.2023-01-01+json"


def test_explicit_accept_operation_header_is_preserved(monkeypatch):
    captured_headers = {}

    def fake_httpx_request(method, url, *, headers, **kwargs):
        captured_headers.update(headers)
        return httpx.Response(200, json={})

    monkeypatch.setattr(httpx, "post", lambda url, *, data, auth: FakeResponse())
    client = AtlasClient.from_service_account(
        client_id="client-id",
        client_secret="client-secret",
    )
    monkeypatch.setattr(
        client._client_wrapper.httpx_client.httpx_client,
        "request",
        fake_httpx_request,
    )

    client._client_wrapper.httpx_client.request(
        "api/atlas/v2/groups/group-id/clusters",
        method="POST",
        headers={
            "content-type": "application/vnd.atlas.2024-10-23+json",
            "Accept": "application/vnd.atlas.2023-01-01+json",
        },
    )

    assert captured_headers["Accept"] == "application/vnd.atlas.2023-01-01+json"


def test_mongodb_atlas_reexports_generated_models():
    assert CloudRegionConfig20240805 is not None


def test_cluster_manager_runs_common_cluster_tasks():
    updates = []

    class FakeClusters:
        def get_cluster(self, group_id, cluster_name):
            return type(
                "Cluster",
                (),
                {
                    "state_name": "IDLE",
                    "replication_specs": [
                        ReplicationSpec20240805(
                            region_configs=[
                                CloudRegionConfig20240805(
                                    electable_specs=HardwareSpec20240805(
                                        instance_size="M10",
                                        disk_size_gb=10.0,
                                        node_count=3,
                                    ),
                                    read_only_specs=DedicatedHardwareSpec20240805(
                                        instance_size="M10",
                                        disk_size_gb=10.0,
                                        node_count=1,
                                    ),
                                    analytics_specs=DedicatedHardwareSpec20240805(
                                        instance_size="M10",
                                        disk_size_gb=10.0,
                                        node_count=1,
                                    ),
                                )
                            ]
                        )
                    ],
                },
            )()

        def update_cluster(self, **kwargs):
            updates.append(kwargs)
            return type("Cluster", (), {"state_name": "IDLE"})()

    manager = ClusterManager(
        client=type("Client", (), {"clusters": FakeClusters()})(),
        project_id="project-id",
        cluster_name="cluster-name",
    )

    manager.pause(wait=False)
    manager.resume(wait=False)
    manager.change_instance_size("M20", wait=False)
    manager.set_disk_autoscaling(True, wait=False)
    manager.change_disk_size(40.0, wait=False)

    assert updates[0] == {
        "group_id_": "project-id",
        "cluster_name": "cluster-name",
        "paused": True,
    }
    assert updates[1] == {
        "group_id_": "project-id",
        "cluster_name": "cluster-name",
        "paused": False,
    }

    instance_size_region = updates[2]["replication_specs"][0].region_configs[0]
    assert instance_size_region.electable_specs.instance_size == "M20"
    assert instance_size_region.read_only_specs.instance_size == "M20"
    assert instance_size_region.analytics_specs.instance_size == "M20"

    disk_autoscaling_region = updates[3]["replication_specs"][0].region_configs[0]
    assert disk_autoscaling_region.auto_scaling.disk_gb.enabled is True

    disk_size_region = updates[4]["replication_specs"][0].region_configs[0]
    assert disk_size_region.electable_specs.disk_size_gb == 40.0
    assert disk_size_region.read_only_specs.disk_size_gb == 40.0
    assert disk_size_region.analytics_specs.disk_size_gb == 40.0


def test_cluster_manager_increases_disk_size_by_gb():
    manager, updates = _cluster_manager_with_disk_size(40.0)

    manager.increase_disk_size(gb=10.0, wait=False)

    disk_size_region = updates[0]["replication_specs"][0].region_configs[0]
    assert disk_size_region.electable_specs.disk_size_gb == 50.0
    assert disk_size_region.read_only_specs.disk_size_gb == 50.0
    assert disk_size_region.analytics_specs.disk_size_gb == 50.0


def test_cluster_manager_increases_disk_size_by_percent():
    manager, updates = _cluster_manager_with_disk_size(40.0)

    manager.increase_disk_size(percent=10.0, wait=False)

    disk_size_region = updates[0]["replication_specs"][0].region_configs[0]
    assert disk_size_region.electable_specs.disk_size_gb == 44.0
    assert disk_size_region.read_only_specs.disk_size_gb == 44.0
    assert disk_size_region.analytics_specs.disk_size_gb == 44.0


def test_increasing_disk_size_without_helper_requires_manual_replication_spec_copying():
    manager, updates = _cluster_manager_with_disk_size(40.0)
    client = manager.client
    project_id = manager.project_id
    cluster_name = manager.cluster_name

    cluster = client.clusters.get_cluster(project_id, cluster_name)
    current_disk_size_gb = cluster.replication_specs[0].region_configs[0].electable_specs.disk_size_gb
    target_disk_size_gb = current_disk_size_gb + 10.0
    updated_replication_specs = [
        spec.model_copy(
            update={
                "region_configs": [
                    region_config.model_copy(
                        update={
                            "electable_specs": region_config.electable_specs.model_copy(
                                update={"disk_size_gb": target_disk_size_gb}
                            ),
                            "read_only_specs": region_config.read_only_specs.model_copy(
                                update={"disk_size_gb": target_disk_size_gb}
                            ),
                            "analytics_specs": region_config.analytics_specs.model_copy(
                                update={"disk_size_gb": target_disk_size_gb}
                            ),
                        }
                    )
                    for region_config in spec.region_configs or []
                ]
            }
        )
        for spec in cluster.replication_specs
    ]
    client.clusters.update_cluster(
        group_id_=project_id,
        cluster_name=cluster_name,
        replication_specs=updated_replication_specs,
    )

    disk_size_region = updates[0]["replication_specs"][0].region_configs[0]
    assert disk_size_region.electable_specs.disk_size_gb == 50.0
    assert disk_size_region.read_only_specs.disk_size_gb == 50.0
    assert disk_size_region.analytics_specs.disk_size_gb == 50.0


def test_cluster_manager_increase_disk_size_requires_one_amount():
    manager, _updates = _cluster_manager_with_disk_size(40.0)

    with pytest.raises(ValueError, match="Provide exactly one"):
        manager.increase_disk_size(wait=False)

    with pytest.raises(ValueError, match="Provide exactly one"):
        manager.increase_disk_size(gb=10.0, percent=10.0, wait=False)


def test_atlas_client_creates_cluster_manager(monkeypatch):
    monkeypatch.setattr(httpx, "post", lambda url, *, data, auth: FakeResponse())
    client = AtlasClient.from_service_account(client_id="client-id", client_secret="client-secret")

    manager = client.cluster("project-id", "cluster-name")

    assert isinstance(manager, ClusterManager)
    assert manager.project_id == "project-id"
    assert manager.cluster_name == "cluster-name"


def _cluster_manager_with_disk_size(disk_size_gb):
    updates = []

    class FakeClusters:
        def get_cluster(self, group_id, cluster_name):
            return type(
                "Cluster",
                (),
                {
                    "state_name": "IDLE",
                    "replication_specs": [
                        ReplicationSpec20240805(
                            region_configs=[
                                CloudRegionConfig20240805(
                                    electable_specs=HardwareSpec20240805(
                                        instance_size="M10",
                                        disk_size_gb=disk_size_gb,
                                        node_count=3,
                                    ),
                                    read_only_specs=DedicatedHardwareSpec20240805(
                                        instance_size="M10",
                                        disk_size_gb=disk_size_gb,
                                        node_count=1,
                                    ),
                                    analytics_specs=DedicatedHardwareSpec20240805(
                                        instance_size="M10",
                                        disk_size_gb=disk_size_gb,
                                        node_count=1,
                                    ),
                                )
                            ]
                        )
                    ],
                },
            )()

        def update_cluster(self, **kwargs):
            updates.append(kwargs)
            return type("Cluster", (), {"state_name": "IDLE"})()

    return (
        ClusterManager(
            client=type("Client", (), {"clusters": FakeClusters()})(),
            project_id="project-id",
            cluster_name="cluster-name",
        ),
        updates,
    )


