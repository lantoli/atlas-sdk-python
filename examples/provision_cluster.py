"""End-to-end Atlas provisioning: project lookup, cluster, db user, IP access.

Mirrors atlas-sdk-go/examples/cluster/aws_cluster/aws.go but uses M10 instead
of M30 to keep demo cost low. The cluster is left running; delete it manually
or with `client.clusters.delete_cluster(...)` when done.

Required env vars:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET

Optional env vars:
    MONGODB_ATLAS_PROJECT_ID
    MONGODB_ATLAS_CLUSTER_NAME
"""

import os
import ipaddress
import secrets
import string
import sys

import httpx

from mongodb_atlas import (
    CloudRegionConfig20240805,
    DatabaseUserRole,
    HardwareSpec20240805,
    NetworkPermissionEntry,
    ReplicationSpec20240805,
)
from _atlas import get_base_url, get_client


def random_suffix(n: int = 5) -> str:
    return "".join(secrets.choice(string.ascii_lowercase) for _ in range(n))


def random_password(n: int = 16) -> str:
    return "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(n))


def project_id_from_env() -> str | None:
    return os.environ.get("MONGODB_ATLAS_PROJECT_ID")


def cluster_name_from_env(suffix_factory=random_suffix) -> str:
    return os.environ.get("MONGODB_ATLAS_CLUSTER_NAME") or f"sdk-demo-{suffix_factory()}"


def get_public_ip(http_get=httpx.get) -> str:
    """Return the public egress IP address for Atlas IP access lists."""
    response = http_get("https://api.ipify.org", timeout=10)
    response.raise_for_status()
    ip_address = response.text.strip()
    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        raise ValueError(f"Expected a valid public IP address, got {ip_address!r}.") from None
    return ip_address


def main() -> None:
    client = get_client()

    project_id = project_id_from_env()
    if project_id is None:
        projects = client.projects.list_groups(items_per_page=1, page_num=1, include_count=True)
        if not projects.results:
            print("Error: no projects found for this service account.")
            sys.exit(1)
        project_id = projects.results[0].id
    print(f"Using project: {project_id}")

    cluster_name = cluster_name_from_env()
    cluster = client.clusters.create_cluster(
        group_id_=project_id,
        name=cluster_name,
        cluster_type="REPLICASET",
        replication_specs=[
            ReplicationSpec20240805(
                region_configs=[
                    CloudRegionConfig20240805(
                        provider_name="AWS",
                        priority=7,
                        region_name="US_EAST_1",
                        electable_specs=HardwareSpec20240805(
                            instance_size="M10",
                            node_count=3,
                        ),
                    )
                ],
            )
        ],
    )
    print(f"Cluster creation initiated: {cluster.name}")

    username = f"sdk-demo-{random_suffix()}"
    client.database_users.create_database_user(
        group_id_=project_id,
        group_id=project_id,
        username=username,
        password=random_password(),
        database_name="admin",
        roles=[DatabaseUserRole(database_name="admin", role_name="readWriteAnyDatabase")],
    )
    print(f"Database user created: {username}")

    local_ip = get_public_ip()
    client.project_ip_access_list.create_access_list_entry(
        group_id=project_id,
        request=[NetworkPermissionEntry(ip_address=local_ip)],
    )
    print(f"IP access entry added: {local_ip}")

    print(f"\nDone. Wait up to 10 minutes for cluster to provision.")
    print(f"Monitor at: {get_base_url()}/v2/{project_id}#/clusters")


if __name__ == "__main__":
    main()
