#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2.32",
# ]
# ///
"""Increase the disk size of a MongoDB Atlas cluster and wait for it to apply.

Authenticates with an Atlas Service Account via OAuth2 client credentials.
Reads configuration from environment variables:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET
    MONGODB_ATLAS_BASE_URL    (e.g. https://cloud.mongodb.com)

Usage:
    uv run resize_disk.py --project-id <projectId> --cluster <name> --gb <amount>
"""

from __future__ import annotations

import argparse
import os
import sys
import time

import requests

API_VERSION = "application/vnd.atlas.2023-01-01+json"
POLL_INTERVAL_SECONDS = 30
POLL_TIMEOUT_SECONDS = 60 * 60


def env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        sys.exit(f"error: missing required env var {name}")
    return value


def get_access_token(base_url: str, client_id: str, client_secret: str) -> str:
    resp = requests.post(
        f"{base_url}/api/oauth/token",
        auth=(client_id, client_secret),
        headers={
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={"grant_type": "client_credentials"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def get_cluster(base_url: str, project_id: str, cluster: str, token: str) -> dict:
    resp = requests.get(
        f"{base_url}/api/atlas/v2/groups/{project_id}/clusters/{cluster}",
        headers={"Accept": API_VERSION, "Authorization": f"Bearer {token}"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def patch_disk_size(
    base_url: str, project_id: str, cluster: str, token: str, disk_size_gb: float
) -> dict:
    resp = requests.patch(
        f"{base_url}/api/atlas/v2/groups/{project_id}/clusters/{cluster}",
        headers={
            "Accept": API_VERSION,
            "Authorization": f"Bearer {token}",
            "Content-Type": API_VERSION,
        },
        json={"diskSizeGB": disk_size_gb},
        timeout=30,
    )
    if not resp.ok:
        sys.exit(f"error: PATCH failed ({resp.status_code}): {resp.text}")
    return resp.json()


def wait_until_idle(
    base_url: str, project_id: str, cluster: str, token: str, target_gb: float
) -> dict:
    deadline = time.monotonic() + POLL_TIMEOUT_SECONDS
    while True:
        info = get_cluster(base_url, project_id, cluster, token)
        state = info.get("stateName", "UNKNOWN")
        current = float(info.get("diskSizeGB", 0))
        print(f"  state={state} diskSizeGB={current}")
        if state == "IDLE" and current >= target_gb:
            return info
        if time.monotonic() >= deadline:
            sys.exit(
                f"error: timed out after {POLL_TIMEOUT_SECONDS}s waiting for cluster "
                f"to reach IDLE with diskSizeGB>={target_gb} (last state={state}, "
                f"diskSizeGB={current})"
            )
        time.sleep(POLL_INTERVAL_SECONDS)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-id", required=True, help="Atlas project (group) ID.")
    parser.add_argument("--cluster", required=True, help="Cluster name to resize.")
    parser.add_argument(
        "--gb",
        type=float,
        required=True,
        help="Number of gigabytes to add to the current disk size.",
    )
    args = parser.parse_args()

    if args.gb <= 0:
        sys.exit("error: --gb must be a positive number")

    base_url = env("MONGODB_ATLAS_BASE_URL").rstrip("/")
    client_id = env("MONGODB_ATLAS_CLIENT_ID")
    client_secret = env("MONGODB_ATLAS_CLIENT_SECRET")

    token = get_access_token(base_url, client_id, client_secret)

    cluster = get_cluster(base_url, args.project_id, args.cluster, token)
    current = float(cluster.get("diskSizeGB", 0))
    if current <= 0:
        sys.exit(
            f"error: could not read current diskSizeGB for cluster {args.cluster!r}"
        )

    target = current + args.gb
    print(
        f"Cluster {args.cluster!r} current diskSizeGB={current}, "
        f"requesting new diskSizeGB={target}."
    )

    patch_disk_size(base_url, args.project_id, args.cluster, token, target)
    print("PATCH accepted. Polling for completion.")

    final = wait_until_idle(base_url, args.project_id, args.cluster, token, target)
    print(
        f"Done. Cluster {args.cluster!r} is IDLE with diskSizeGB="
        f"{final.get('diskSizeGB')}."
    )


if __name__ == "__main__":
    main()
