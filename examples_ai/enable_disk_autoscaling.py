#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Enable disk auto-scaling on an Atlas MongoDB cluster and wait for completion."""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ATLAS_API_VERSION = "2024-08-05"
POLL_INTERVAL_SECONDS = 15
POLL_TIMEOUT_SECONDS = 60 * 60


def get_access_token(base_url: str, client_id: str, client_secret: str) -> str:
    creds = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    data = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode()
    req = urllib.request.Request(
        f"{base_url}/api/oauth/token",
        data=data,
        method="POST",
        headers={
            "Authorization": f"Basic {creds}",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())["access_token"]


def atlas_request(
    method: str,
    url: str,
    token: str,
    body: dict | None = None,
) -> dict:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": f"application/vnd.atlas.{ATLAS_API_VERSION}+json",
    }
    data = None
    if body is not None:
        headers["Content-Type"] = f"application/vnd.atlas.{ATLAS_API_VERSION}+json"
        data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        sys.stderr.write(f"HTTP {e.code} on {method} {url}: {e.read().decode()}\n")
        raise


def build_autoscaling_patch(cluster: dict) -> dict:
    """Return a minimal PATCH payload that enables disk GB auto-scaling on every region."""
    replication_specs = []
    for spec in cluster["replicationSpecs"]:
        region_configs = []
        for region in spec["regionConfigs"]:
            auto_scaling = dict(region.get("autoScaling", {}))
            auto_scaling["diskGB"] = {"enabled": True}
            new_region = {
                "providerName": region["providerName"],
                "regionName": region["regionName"],
                "priority": region["priority"],
                "autoScaling": auto_scaling,
            }
            for key in ("electableSpecs", "readOnlySpecs", "analyticsSpecs", "backingProviderName"):
                if key in region:
                    new_region[key] = region[key]
            region_configs.append(new_region)
        replication_specs.append({"id": spec["id"], "regionConfigs": region_configs})
    return {"replicationSpecs": replication_specs}


def wait_until_idle(base_url: str, token: str, project_id: str, cluster_name: str) -> None:
    cluster_url = (
        f"{base_url}/api/atlas/v2/groups/{project_id}/clusters/"
        f"{urllib.parse.quote(cluster_name)}"
    )
    deadline = time.monotonic() + POLL_TIMEOUT_SECONDS
    while True:
        state = atlas_request("GET", cluster_url, token)["stateName"]
        print(f"  cluster state: {state}")
        if state == "IDLE":
            return
        if time.monotonic() > deadline:
            raise TimeoutError(f"Cluster {cluster_name} did not reach IDLE within timeout.")
        time.sleep(POLL_INTERVAL_SECONDS)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_id", help="Atlas project (group) ID.")
    parser.add_argument("cluster_name", help="Atlas cluster name.")
    args = parser.parse_args()

    try:
        client_id = os.environ["MONGODB_ATLAS_CLIENT_ID"]
        client_secret = os.environ["MONGODB_ATLAS_CLIENT_SECRET"]
        base_url = os.environ["MONGODB_ATLAS_BASE_URL"].rstrip("/")
    except KeyError as missing:
        sys.stderr.write(f"Missing required environment variable: {missing.args[0]}\n")
        return 2

    print("Authenticating with Atlas service account.")
    token = get_access_token(base_url, client_id, client_secret)

    cluster_url = (
        f"{base_url}/api/atlas/v2/groups/{args.project_id}/clusters/"
        f"{urllib.parse.quote(args.cluster_name)}"
    )

    print(f"Fetching cluster {args.cluster_name}.")
    cluster = atlas_request("GET", cluster_url, token)

    already_enabled = all(
        region.get("autoScaling", {}).get("diskGB", {}).get("enabled")
        for spec in cluster["replicationSpecs"]
        for region in spec["regionConfigs"]
    )
    if already_enabled:
        print("Disk auto-scaling is already enabled on every region. Nothing to do.")
        return 0

    patch = build_autoscaling_patch(cluster)
    print("Enabling disk auto-scaling.")
    atlas_request("PATCH", cluster_url, token, body=patch)

    print("Waiting for cluster to return to IDLE.")
    wait_until_idle(base_url, token, args.project_id, args.cluster_name)
    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
