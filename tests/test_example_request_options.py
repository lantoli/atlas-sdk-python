import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "examples"))

from _atlas import get_base_url
from provision_cluster import cluster_name_from_env, get_public_ip, project_id_from_env


class FakeIpResponse:
    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        pass


def test_provision_cluster_passes_database_user_body_group_id():
    source = Path("examples/provision_cluster.py").read_text()
    call = source.split("client.database_users.create_database_user(", maxsplit=1)[1].split(
        "    )", maxsplit=1
    )[0]
    assert "group_id=project_id" in call


def test_get_base_url_uses_env_var(monkeypatch):
    monkeypatch.setenv("MONGODB_ATLAS_BASE_URL", "https://cloud-dev.mongodb.com")
    assert get_base_url() == "https://cloud-dev.mongodb.com"


def test_provision_cluster_monitor_url_uses_base_url():
    source = Path("examples/provision_cluster.py").read_text()
    assert "atlas_request_options" not in source
    assert "request_options=" not in source
    assert "from _atlas import get_base_url, get_client" in source
    assert 'print(f"Monitor at: {get_base_url()}/v2/{project_id}#/clusters")' in source


def test_pause_cluster_does_not_pass_version_request_options():
    source = Path("examples/pause_cluster.py").read_text()
    assert "atlas_request_options" not in source
    assert "request_options=" not in source


def test_manage_cluster_example_uses_cluster_manager():
    source = Path("examples/manage_cluster.py").read_text()
    assert "get_client()" in source
    assert "client.cluster(project_id, cluster_name)" in source
    assert "MONGODB_ATLAS_CLUSTER_ACTION" not in source
    assert "cluster_manager_commands" not in source
    assert "print(" not in source
    assert "if action" not in source
    assert "elif action" not in source
    assert ".update_cluster(" not in source


def test_manage_cluster_example_calls_demo_commands(capsys, monkeypatch):
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "examples"))
    import manage_cluster

    calls = []

    class FakeCluster:
        def pause(self):
            calls.append(("pause",))

        def resume(self):
            calls.append(("resume",))

        def change_instance_size(self, instance_size):
            calls.append(("change_instance_size", instance_size))

        def set_disk_autoscaling(self, enabled):
            calls.append(("set_disk_autoscaling", enabled))

        def increase_disk_size(self, **kwargs):
            calls.append(("increase_disk_size", kwargs))

    class FakeClient:
        def cluster(self, project_id, cluster_name):
            calls.append(("cluster", project_id, cluster_name))
            return FakeCluster()

    monkeypatch.setenv("MONGODB_ATLAS_PROJECT_ID", "project-id")
    monkeypatch.setenv("MONGODB_ATLAS_CLUSTER_NAME", "cluster-name")
    monkeypatch.setattr(manage_cluster, "get_client", lambda: FakeClient())

    manage_cluster.main()

    assert capsys.readouterr().out == ""
    assert calls == [
        ("cluster", "project-id", "cluster-name"),
        ("pause",),
        ("resume",),
        ("change_instance_size", "M20"),
        ("set_disk_autoscaling", True),
        ("set_disk_autoscaling", False),
        ("increase_disk_size", {"gb": 10}),
        ("increase_disk_size", {"percent": 10}),
        ("increase_disk_size", {"percent": 10, "wait": False}),
        ("increase_disk_size", {"percent": 10, "wait": True}),
    ]


def test_provision_cluster_reads_project_id_from_env(monkeypatch):
    monkeypatch.setenv("MONGODB_ATLAS_PROJECT_ID", "project-id")
    assert project_id_from_env() == "project-id"


def test_provision_cluster_reads_cluster_name_from_env(monkeypatch):
    monkeypatch.setenv("MONGODB_ATLAS_CLUSTER_NAME", "cluster-name")
    assert cluster_name_from_env() == "cluster-name"


def test_provision_cluster_cluster_name_falls_back_to_random(monkeypatch):
    monkeypatch.delenv("MONGODB_ATLAS_CLUSTER_NAME", raising=False)
    assert cluster_name_from_env(lambda: "abcde") == "sdk-demo-abcde"


def test_get_public_ip_uses_public_echo_service():
    calls = []

    def fake_get(url, *, timeout):
        calls.append((url, timeout))
        return FakeIpResponse("203.0.113.42\n")

    assert get_public_ip(http_get=fake_get) == "203.0.113.42"
    assert calls == [("https://api.ipify.org", 10)]


def test_get_public_ip_rejects_invalid_response():
    def fake_get(url, *, timeout):
        return FakeIpResponse("not-an-ip")

    with pytest.raises(ValueError, match="valid public IP"):
        get_public_ip(http_get=fake_get)
