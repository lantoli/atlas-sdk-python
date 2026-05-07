"""Provision a geosharded multi-cloud Atlas cluster.

Mirrors a larger Terraform `mongodbatlas_advanced_cluster` shape with two
zones, two shards per zone, and AWS plus Azure region configs.

Required env vars:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET
    MONGODB_ATLAS_PROJECT_ID
    MONGODB_ATLAS_CLUSTER_NAME
"""

import os

from mongodb_atlas import CloudRegionConfig20240805, HardwareSpec20240805, ReplicationSpec20240805

from _atlas import get_base_url, get_client


def region_config(
    *,
    provider_name: str,
    region_name: str,
    priority: int,
    node_count: int,
    instance_size: str = "M10",
) -> CloudRegionConfig20240805:
    return CloudRegionConfig20240805(
        provider_name=provider_name,
        priority=priority,
        region_name=region_name,
        electable_specs=HardwareSpec20240805(
            instance_size=instance_size,
            node_count=node_count,
        ),
    )


def shard_spec(zone_name: str, aws_region: str, azure_region: str) -> ReplicationSpec20240805:
    return ReplicationSpec20240805(
        zone_name=zone_name,
        region_configs=[
            region_config(
                provider_name="AWS",
                region_name=aws_region,
                priority=7,
                node_count=3,
            ),
            region_config(
                provider_name="AZURE",
                region_name=azure_region,
                priority=6,
                node_count=2,
            ),
        ],
    )


def build_replication_specs() -> list[ReplicationSpec20240805]:
    return [
        # shard 1 - zone n1.
        shard_spec("zone n1", "US_WEST_2", "US_EAST_2"),
        # shard 2 - zone n1.
        shard_spec("zone n1", "US_WEST_2", "US_EAST_2"),
        # shard 1 - zone n2.
        shard_spec("zone n2", "EU_WEST_1", "EUROPE_NORTH"),
        # shard 2 - zone n2.
        shard_spec("zone n2", "EU_WEST_1", "EUROPE_NORTH"),
    ]


def main() -> None:
    project_id = os.environ["MONGODB_ATLAS_PROJECT_ID"]
    cluster_name = os.environ["MONGODB_ATLAS_CLUSTER_NAME"]

    client = get_client()
    cluster = client.clusters.create_cluster(
        group_id_=project_id,
        name=cluster_name,
        cluster_type="GEOSHARDED",
        replication_specs=build_replication_specs(),
    )

    print(f"Big cluster creation initiated: {cluster.name}")
    print(f"Monitor at: {get_base_url()}/v2/{project_id}#/clusters")


if __name__ == "__main__":
    main()
