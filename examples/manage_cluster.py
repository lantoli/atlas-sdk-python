"""Show common Atlas cluster changes through the ClusterManager helper.

Required env vars:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET
    MONGODB_ATLAS_PROJECT_ID
    MONGODB_ATLAS_CLUSTER_NAME
"""

from __future__ import annotations

import os

from _atlas import get_client


def main() -> None:
    project_id = os.environ["MONGODB_ATLAS_PROJECT_ID"]
    cluster_name = os.environ["MONGODB_ATLAS_CLUSTER_NAME"]

    client = get_client()
    cluster = client.cluster(project_id, cluster_name)

    cluster.pause()
    cluster.resume()
    cluster.change_instance_size("M20")
    cluster.set_disk_autoscaling(True)
    cluster.set_disk_autoscaling(False)
    cluster.increase_disk_size(gb=10)
    cluster.increase_disk_size(percent=10)
    cluster.increase_disk_size(percent=10, wait=False)
    cluster.increase_disk_size(percent=10, wait=True)

if __name__ == "__main__":
    main()
