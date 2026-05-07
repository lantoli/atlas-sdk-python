"""Pause and unpause an Atlas cluster.

Demonstrates the PATCH semantics of update_cluster: send only the field you
want to change. The Atlas API returns immediately while the cluster transitions
through PAUSING then IDLE states. This example polls get_cluster until
state_name == "IDLE" before issuing the next update.

Required env vars:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET
    MONGODB_ATLAS_PROJECT_ID
    MONGODB_ATLAS_CLUSTER_NAME
"""

import os
import time
from collections.abc import Callable
from typing import Any

from _atlas import get_client


def wait_for_cluster_state(
    *,
    client: Any,
    project_id: str,
    cluster_name: str,
    target_state: str,
    timeout_seconds: int = 1800,
    poll_seconds: int = 30,
    sleep: Callable[[int], None] = time.sleep,
) -> Any:
    """Poll until the cluster reaches the target state."""
    deadline = time.monotonic() + timeout_seconds
    while True:
        cluster = client.clusters.get_cluster(project_id, cluster_name)
        if cluster.state_name == target_state:
            return cluster
        if time.monotonic() >= deadline:
            raise TimeoutError(
                f"Cluster {cluster_name} did not reach {target_state}; last state was {cluster.state_name}."
            )
        print(f"Cluster state is {cluster.state_name}; waiting {poll_seconds} seconds...")
        sleep(poll_seconds)


def main() -> None:
    project_id = os.environ["MONGODB_ATLAS_PROJECT_ID"]
    cluster_name = os.environ["MONGODB_ATLAS_CLUSTER_NAME"]

    client = get_client()

    paused = client.clusters.update_cluster(
        group_id_=project_id,
        cluster_name=cluster_name,
        paused=True,
    )
    print(f"Pause initiated. Cluster: {paused.name}, paused: {paused.paused}")
    wait_for_cluster_state(
        client=client,
        project_id=project_id,
        cluster_name=cluster_name,
        target_state="IDLE",
    )

    unpaused = client.clusters.update_cluster(
        group_id_=project_id,
        cluster_name=cluster_name,
        paused=False,
    )
    print(f"Unpause initiated. Cluster: {unpaused.name}, paused: {unpaused.paused}")
    wait_for_cluster_state(
        client=client,
        project_id=project_id,
        cluster_name=cluster_name,
        target_state="IDLE",
    )


if __name__ == "__main__":
    main()
