"""Toggle compute and disk autoscaling for an Atlas cluster, then wait for IDLE.

Required env vars:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET
    MONGODB_ATLAS_PROJECT_ID
    MONGODB_ATLAS_CLUSTER_NAME
    MONGODB_ATLAS_AUTOSCALING_ENABLED

Required when MONGODB_ATLAS_AUTOSCALING_ENABLED is true:
    MONGODB_ATLAS_AUTOSCALING_MIN_INSTANCE_SIZE
    MONGODB_ATLAS_AUTOSCALING_MAX_INSTANCE_SIZE

Optional env vars:
    MONGODB_ATLAS_AUTOSCALING_SCALE_DOWN_ENABLED
    MONGODB_ATLAS_DISK_AUTOSCALING_ENABLED
"""

from __future__ import annotations

import os
from typing import Any

from mongodb_atlas import AdvancedAutoScalingSettings, AdvancedComputeAutoScaling, DiskGbAutoScaling

from _atlas import get_client
from pause_cluster import wait_for_cluster_state


def parse_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n"}:
        return False
    raise ValueError(f"Expected a boolean value, got {value!r}.")


def copy_model(model: Any, **updates: Any) -> Any:
    if hasattr(model, "model_copy"):
        return model.model_copy(update=updates)
    return model.copy(update=updates)


def region_config_with_auto_scaling(
    region_config: Any,
    *,
    enabled: bool,
    min_instance_size: str | None,
    max_instance_size: str | None,
    scale_down_enabled: bool,
    disk_enabled: bool,
) -> Any:
    return copy_model(
        region_config,
        auto_scaling=AdvancedAutoScalingSettings(
            compute=AdvancedComputeAutoScaling(
                enabled=enabled,
                min_instance_size=min_instance_size,
                max_instance_size=max_instance_size,
                scale_down_enabled=scale_down_enabled,
            ),
            disk_gb=DiskGbAutoScaling(enabled=disk_enabled),
        ),
    )


def replication_specs_with_auto_scaling(
    replication_specs: list[Any],
    *,
    enabled: bool,
    min_instance_size: str | None,
    max_instance_size: str | None,
    scale_down_enabled: bool,
    disk_enabled: bool,
) -> list[Any]:
    if not replication_specs:
        raise ValueError("Cluster has no replication specs to update.")

    updated_specs = []
    for spec in replication_specs:
        region_configs = spec.region_configs or []
        updated_specs.append(
            copy_model(
                spec,
                region_configs=[
                    region_config_with_auto_scaling(
                        region_config,
                        enabled=enabled,
                        min_instance_size=min_instance_size,
                        max_instance_size=max_instance_size,
                        scale_down_enabled=scale_down_enabled,
                        disk_enabled=disk_enabled,
                    )
                    for region_config in region_configs
                ],
            )
        )
    return updated_specs


def require_autoscaling_bounds(enabled: bool) -> tuple[str | None, str | None]:
    if not enabled:
        return None, None
    return (
        os.environ["MONGODB_ATLAS_AUTOSCALING_MIN_INSTANCE_SIZE"],
        os.environ["MONGODB_ATLAS_AUTOSCALING_MAX_INSTANCE_SIZE"],
    )


def main() -> None:
    project_id = os.environ["MONGODB_ATLAS_PROJECT_ID"]
    cluster_name = os.environ["MONGODB_ATLAS_CLUSTER_NAME"]
    enabled = parse_bool(os.environ["MONGODB_ATLAS_AUTOSCALING_ENABLED"])
    min_instance_size, max_instance_size = require_autoscaling_bounds(enabled)
    scale_down_enabled = parse_bool(
        os.environ.get("MONGODB_ATLAS_AUTOSCALING_SCALE_DOWN_ENABLED", "false")
    )
    disk_enabled = parse_bool(os.environ.get("MONGODB_ATLAS_DISK_AUTOSCALING_ENABLED", str(enabled)))

    client = get_client()
    cluster = client.clusters.get_cluster(project_id, cluster_name)
    updated_specs = replication_specs_with_auto_scaling(
        cluster.replication_specs,
        enabled=enabled,
        min_instance_size=min_instance_size,
        max_instance_size=max_instance_size,
        scale_down_enabled=scale_down_enabled,
        disk_enabled=disk_enabled,
    )

    updated = client.clusters.update_cluster(
        group_id_=project_id,
        cluster_name=cluster_name,
        replication_specs=updated_specs,
    )
    print(f"Autoscaling update initiated. Cluster: {updated.name}, enabled: {enabled}")
    wait_for_cluster_state(
        client=client,
        project_id=project_id,
        cluster_name=cluster_name,
        target_state="IDLE",
    )


if __name__ == "__main__":
    main()
