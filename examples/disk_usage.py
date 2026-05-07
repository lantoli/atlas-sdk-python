"""Show configured and used disk size for an Atlas cluster.

Required env vars:
    MONGODB_ATLAS_CLIENT_ID.
    MONGODB_ATLAS_CLIENT_SECRET.
    MONGODB_ATLAS_PROJECT_ID.
    MONGODB_ATLAS_CLUSTER_NAME.
"""

from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Any

from _atlas import get_client

BYTES_PER_GB = 1024**3
DISK_USED = "DISK_PARTITION_SPACE_USED"
DISK_FREE = "DISK_PARTITION_SPACE_FREE"


@dataclass(frozen=True)
class DiskUsage:
    process_id: str
    partition_name: str
    used_bytes: float | None
    free_bytes: float | None


def cluster_processes(processes: list[Any], cluster_name: str) -> list[Any]:
    """Return processes whose host labels appear to belong to the cluster."""
    needle = cluster_name.lower()
    return [
        process
        for process in processes
        if any(needle in value.lower() for value in _process_labels(process))
    ]


def disk_size_gb(cluster: Any) -> float:
    """Return the first configured disk size from the cluster replication specs."""
    for spec in cluster.replication_specs or []:
        for region_config in spec.region_configs or []:
            for hardware_spec in (
                region_config.electable_specs,
                region_config.read_only_specs,
                region_config.analytics_specs,
            ):
                if hardware_spec is not None and hardware_spec.disk_size_gb is not None:
                    return hardware_spec.disk_size_gb
    raise RuntimeError("Cluster has no configured disk size.")


def latest_disk_values(measurements: Any) -> dict[str, float]:
    """Return the latest non-null values from disk measurement series."""
    values: dict[str, float] = {}
    for measurement in measurements.measurements or []:
        if measurement.name not in {DISK_USED, DISK_FREE}:
            continue
        for data_point in reversed(measurement.data_points or []):
            if data_point.value is not None:
                values[measurement.name] = data_point.value
                break
    return values


def bytes_to_gb(value: float) -> float:
    """Convert bytes to gibibytes."""
    return value / BYTES_PER_GB


def configured_disk_line(configured_disk_gb: float, usages: list[DiskUsage]) -> str:
    """Return the configured disk summary with the most-used disk."""
    most_used = max(
        (usage for usage in usages if usage.used_bytes is not None),
        key=lambda usage: usage.used_bytes or 0,
        default=None,
    )
    line = f"Configured disk size: {configured_disk_gb:.1f} GB"
    if most_used is None:
        return line

    used_gb = bytes_to_gb(most_used.used_bytes or 0)
    suffix = f"Most used disk: {most_used.process_id} ({most_used.partition_name}), {used_gb:.1f} GB used"
    if most_used.free_bytes is not None:
        used_percent = most_used.used_bytes / (most_used.used_bytes + most_used.free_bytes) * 100
        suffix = f"{suffix}, {used_percent:.1f}%"
    return f"{line}. {suffix}."


def main() -> None:
    project_id = os.environ["MONGODB_ATLAS_PROJECT_ID"]
    cluster_name = os.environ["MONGODB_ATLAS_CLUSTER_NAME"]

    client = get_client()
    cluster = client.clusters.get_cluster(project_id, cluster_name)
    configured_disk_gb = disk_size_gb(cluster)

    processes = client.monitoring_and_logs.list_group_processes(
        project_id,
        items_per_page=500,
    ).results or []
    matched_processes = cluster_processes(processes, cluster_name)
    if not matched_processes:
        raise RuntimeError(f"No MongoDB processes found for cluster {cluster_name}.")

    usages: list[DiskUsage] = []
    for process in matched_processes:
        process_id = process.id
        if process_id is None:
            continue

        partition_name = _data_partition_name(client, project_id, process_id)
        measurements = client.monitoring_and_logs.get_process_disk_measurements(
            project_id,
            process_id,
            partition_name,
            granularity="PT1H",
            period="P1D",
            m=[DISK_USED, DISK_FREE],
        )
        values = latest_disk_values(measurements)
        usages.append(
            DiskUsage(
                process_id=process_id,
                partition_name=partition_name,
                used_bytes=values.get(DISK_USED),
                free_bytes=values.get(DISK_FREE),
            )
        )

    print(f"Cluster: {cluster_name}")
    print(configured_disk_line(configured_disk_gb, usages))
    print("")

    for usage in usages:
        if usage.used_bytes is None:
            print(f"{usage.process_id} ({usage.partition_name}): no used disk measurement returned.")
            continue

        used_gb = bytes_to_gb(usage.used_bytes)
        if usage.free_bytes is None:
            print(f"{usage.process_id} ({usage.partition_name}): used {used_gb:.1f} GB.")
            continue

        free_gb = bytes_to_gb(usage.free_bytes)
        used_percent = usage.used_bytes / (usage.used_bytes + usage.free_bytes) * 100
        print(
            f"{usage.process_id} ({usage.partition_name}): "
            f"used {used_gb:.1f} GB, free {free_gb:.1f} GB, used {used_percent:.1f}%."
        )


def _process_labels(process: Any) -> list[str]:
    return [
        value
        for value in (
            getattr(process, "id", None),
            getattr(process, "hostname", None),
            getattr(process, "user_alias", None),
            getattr(process, "replica_set_name", None),
            getattr(process, "shard_name", None),
        )
        if isinstance(value, str)
    ]


def _data_partition_name(client: Any, project_id: str, process_id: str) -> str:
    disks = client.monitoring_and_logs.list_process_disks(project_id, process_id).results or []
    for disk in disks:
        if disk.partition_name == "data":
            return "data"
    for disk in disks:
        if disk.partition_name:
            return disk.partition_name
    raise RuntimeError(f"No disk partitions found for process {process_id}.")


if __name__ == "__main__":
    main()
