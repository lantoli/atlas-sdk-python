"""Shared helper for the example scripts.

Constructs an AtlasClient using service account credentials from environment
variables and exposes small utilities shared by multiple examples.

Usage:
    from _atlas import get_client
    client = get_client()
    client.projects.list_groups()

Required env vars:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET

Optional env vars:
    MONGODB_ATLAS_BASE_URL  (defaults to https://cloud.mongodb.com)
"""

import os

from mongodb_atlas import (
    AtlasClient,
    fetch_service_account_token,
    get_base_url,
)


def get_token() -> str:
    """Fetch a bearer token using OAuth2 client credentials flow."""
    return fetch_service_account_token(
        client_id=os.environ["MONGODB_ATLAS_CLIENT_ID"],
        client_secret=os.environ["MONGODB_ATLAS_CLIENT_SECRET"],
        base_url=get_base_url(),
    )


def get_client() -> AtlasClient:
    """Return an AtlasClient authenticated with a fresh OAuth token."""
    return AtlasClient.from_env()


def get_org_id(client: AtlasClient) -> str:
    """Return the org ID associated with the service account credentials."""
    projects = client.projects.list_groups(items_per_page=1, page_num=1)
    if not projects.results:
        raise RuntimeError("No projects found for this service account.")
    return projects.results[0].org_id
