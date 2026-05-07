#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2.32",
# ]
# ///
"""Change the instance size of all nodes in a MongoDB Atlas cluster.

Updates electable, read-only, and analytics specs across every region config in
every replication spec to the requested instance size (e.g. M30, M40), then
waits for the cluster to return to the IDLE state.

Authenticates with an Atlas Service Account via OAuth2 client credentials.
Reads configuration from environment variables:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET
    MONGODB_ATLAS_BASE_URL    (e.g. https://cloud.mongodb.com)

Usage:
    uv run resize_instance.py --project-id <projectId> --cluster <name> --size <M30>
"""

from __future__ import annotations

import argparse
import os
import sys
import time

import requests

API_VERSION = "application/vnd.atlas.2024-08-05+json"
SPEC_KEYS = ("electableSpecs", "readOnlySpecs", "analyticsSpecs")
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


def collect_instance_sizes(replication_specs: list[dict]) -> set[str]:
    sizes: set[str] = set()
    for spec in replication_specs:
        for region in spec.get("regionConfigs", []):
            for key in SPEC_KEYS:
                node_spec = region.get(key)
                if node_spec and int(node_spec.get("nodeCount", 0)) > 0:
                    size = node_spec.get("instanceSize")
                    if size:
                        sizes.add(size)
    return sizes


def build_resized_specs(replication_specs: list[dict], new_size: str) -> list[dict]:
    updated: list[dict] = []
    for spec in replication_specs:
        new_regions = []
        for region in spec.get("regionConfigs", []):
            new_region = dict(region)
            for key in SPEC_KEYS:
                node_spec = region.get(key)
                if node_spec and int(node_spec.get("nodeCount", 0)) > 0:
                    new_region[key] = {**node_spec, "instanceSize": new_size}
            new_regions.append(new_region)
        updated.append({**spec, "regionConfigs": new_regions})
    return updated


def patch_instance_size(
    base_url: str,
    project_id: str,
    cluster: str,
    token: str,
    replication_specs: list[dict],
) -> dict:
    resp = requests.patch(
        f"{base_url}/api/atlas/v2/groups/{project_id}/clusters/{cluster}",
        headers={
            "Accept": API_VERSION,
            "Authorization": f"Bearer {token}",
            "Content-Type": API_VERSION,
        },
        json={"replicationSpecs": replication_specs},
        timeout=30,
    )
    if not resp.ok:
        sys.exit(f"error: PATCH failed ({resp.status_code}): {resp.text}")
    return resp.json()


def wait_until_idle(
    base_url: str, project_id: str, cluster: str, token: str, target_size: str
) -> dict:
    deadline = time.monotonic() + POLL_TIMEOUT_SECONDS
    while True:
        info = get_cluster(base_url, project_id, cluster, token)
        state = info.get("stateName", "UNKNOWN")
        sizes = collect_instance_sizes(info.get("replicationSpecs", []))
        print(f"  state={state} instanceSizes={sorted(sizes) or ['?']}")
        if state == "IDLE" and sizes == {target_size}:
            return info
        if time.monotonic() >= deadline:
            sys.exit(
                f"error: timed out after {POLL_TIMEOUT_SECONDS}s waiting for cluster "
                f"to reach IDLE with instanceSize={target_size} "
                f"(last state={state}, sizes={sorted(sizes)})"
            )
        time.sleep(POLL_INTERVAL_SECONDS)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-id", required=True, help="Atlas project (group) ID.")
    parser.add_argument("--cluster", required=True, help="Cluster name to resize.")
    parser.add_argument(
        "--size",
        required=True,
        help="New instance size to apply to every node (e.g. M30, M40, M50).",
    )
    args = parser.parse_args()

    new_size = args.size.strip().upper()
    if not new_size.startswith("M") or not new_size[1:].split("_")[0].isdigit():
        sys.exit(f"error: --size {args.size!r} is not a valid Atlas instance size")

    base_url = env("MONGODB_ATLAS_BASE_URL").rstrip("/")
    client_id = env("MONGODB_ATLAS_CLIENT_ID")
    client_secret = env("MONGODB_ATLAS_CLIENT_SECRET")

    token = get_access_token(base_url, client_id, client_secret)

    cluster = get_cluster(base_url, args.project_id, args.cluster, token)
    replication_specs = cluster.get("replicationSpecs") or []
    if not replication_specs:
        sys.exit(
            f"error: cluster {args.cluster!r} has no replicationSpecs to update"
        )

    current_sizes = collect_instance_sizes(replication_specs)
    print(
        f"Cluster {args.cluster!r} current instanceSizes={sorted(current_sizes)}, "
        f"requesting new instanceSize={new_size}."
    )

    if current_sizes == {new_size}:
        print(f"Already at {new_size}, nothing to do.")
        return

    updated_specs = build_resized_specs(replication_specs, new_size)
    patch_instance_size(base_url, args.project_id, args.cluster, token, updated_specs)
    print("PATCH accepted. Polling for completion.")

    final = wait_until_idle(base_url, args.project_id, args.cluster, token, new_size)
    final_sizes = collect_instance_sizes(final.get("replicationSpecs", []))
    print(
        f"Done. Cluster {args.cluster!r} is IDLE with instanceSizes="
        f"{sorted(final_sizes)}."
    )


if __name__ == "__main__":
    main()
