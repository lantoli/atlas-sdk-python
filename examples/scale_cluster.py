"""Scale an Atlas cluster by changing its instance size.

Required env vars:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET
    MONGODB_ATLAS_PROJECT_ID
    MONGODB_ATLAS_CLUSTER_NAME
    MONGODB_ATLAS_INSTANCE_SIZE
"""

from __future__ import annotations

import os
from typing import Any

from _atlas import get_client


def copy_model(model: Any, **updates: Any) -> Any:
    if hasattr(model, "model_copy"):
        return model.model_copy(update=updates)
    return model.copy(update=updates)


def with_instance_size(spec: Any, instance_size: str) -> Any:
    if spec is None:
        return None
    return copy_model(spec, instance_size=instance_size)


def region_config_with_instance_size(region_config: Any, instance_size: str) -> Any:
    return copy_model(
        region_config,
        electable_specs=with_instance_size(region_config.electable_specs, instance_size),
        read_only_specs=with_instance_size(region_config.read_only_specs, instance_size),
        analytics_specs=with_instance_size(region_config.analytics_specs, instance_size),
    )


def replication_specs_with_instance_size(replication_specs: list[Any], instance_size: str) -> list[Any]:
    if not replication_specs:
        raise ValueError("Cluster has no replication specs to update.")

    updated_specs = []
    for spec in replication_specs:
        region_configs = spec.region_configs or []
        updated_specs.append(
            copy_model(
                spec,
                region_configs=[
                    region_config_with_instance_size(region_config, instance_size)
                    for region_config in region_configs
                ],
            )
        )
    return updated_specs


def main() -> None:
    project_id = os.environ["MONGODB_ATLAS_PROJECT_ID"]
    cluster_name = os.environ["MONGODB_ATLAS_CLUSTER_NAME"]
    instance_size = os.environ["MONGODB_ATLAS_INSTANCE_SIZE"]

    client = get_client()
    cluster = client.clusters.get_cluster(project_id, cluster_name)
    updated_specs = replication_specs_with_instance_size(cluster.replication_specs, instance_size)

    updated = client.clusters.update_cluster(
        group_id_=project_id,
        cluster_name=cluster_name,
        replication_specs=updated_specs,
    )
    print(f"Scale initiated. Cluster: {updated.name}, target instance size: {instance_size}")


if __name__ == "__main__":
    main()
