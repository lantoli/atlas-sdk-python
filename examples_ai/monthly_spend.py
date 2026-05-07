#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2.32",
# ]
# ///
"""Show monthly spend by service category for a MongoDB Atlas organization.

Authenticates with an Atlas Service Account via OAuth2 client credentials.
Reads configuration from environment variables:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET
    MONGODB_ATLAS_BASE_URL    (e.g. https://cloud.mongodb.com)
    MONGODB_ATLAS_ORG_ID

Usage:
    uv run monthly_spend.py [--json] [--show-unmapped]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone

import requests

API_VERSION = "application/vnd.atlas.2023-01-01+json"
PAGE_SIZE = 100

# Order matters: first matching rule wins. Tokens are matched as substrings
# against the line item SKU (case-insensitive).
CATEGORY_RULES: list[tuple[str, tuple[str, ...]]] = [
    ("Private Endpoint", ("PRIVATE_ENDPOINT", "PRIVATE_LINK", "PRIVATELINK")),
    ("Stream Processing", ("STREAM_PROCESSING", "STREAM_PROCESSOR", "ATLAS_STREAMS")),
    ("Atlas Search", ("ATLAS_SEARCH", "ATLAS_FTS")),
    ("BI Connector", ("BI_CONNECTOR",)),
    ("Auditing", ("AUDIT",)),
    ("Advanced Security", (
        "ADVANCED_SECURITY",
        "BYO_KMS",
        "KMS_KEY",
        "X509",
        "LDAPS",
    )),
    ("Data Transfer", ("DATA_TRANSFER",)),
    ("Storage", ("STORAGE", "DISK_IOPS", "PROVISIONED_IOPS")),
    ("Clusters", (
        "INSTANCE",
        "REPLICA_SET",
        "SHARD",
        "SERVERLESS",
        "FLEX",
        "BACKUP",
        "SNAPSHOT",
        "PIT_RESTORE",
    )),
]
CATEGORY_ORDER = [name for name, _ in CATEGORY_RULES] + ["Other"]


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


def parse_date(value: str) -> date:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).date()


def list_invoices(base_url: str, org_id: str, token: str, since: date) -> list[dict]:
    invoices: list[dict] = []
    page = 1
    headers = {"Accept": API_VERSION, "Authorization": f"Bearer {token}"}
    url = f"{base_url}/api/atlas/v2/orgs/{org_id}/invoices"

    while True:
        resp = requests.get(
            url,
            headers=headers,
            params={"pageNum": page, "itemsPerPage": PAGE_SIZE, "viewLinkedInvoices": "false"},
            timeout=30,
        )
        resp.raise_for_status()
        results = resp.json().get("results", [])
        if not results:
            break
        invoices.extend(results)
        oldest = min(parse_date(inv["startDate"]) for inv in results)
        if oldest < since or len(results) < PAGE_SIZE:
            break
        page += 1

    return [inv for inv in invoices if parse_date(inv["startDate"]) >= since]


def fetch_invoice(base_url: str, org_id: str, token: str, invoice_id: str) -> dict:
    headers = {"Accept": API_VERSION, "Authorization": f"Bearer {token}"}
    resp = requests.get(
        f"{base_url}/api/atlas/v2/orgs/{org_id}/invoices/{invoice_id}",
        headers=headers,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def categorize(sku: str) -> str:
    upper = sku.upper()
    for name, tokens in CATEGORY_RULES:
        if any(token in upper for token in tokens):
            return name
    return "Other"


def build_matrix(
    invoices: list[dict],
) -> tuple[dict[str, dict[str, int]], dict[str, set[str]]]:
    by_month: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    unmapped: dict[str, set[str]] = defaultdict(set)

    for inv in invoices:
        month = parse_date(inv["startDate"]).strftime("%Y-%m")
        for item in inv.get("lineItems") or []:
            sku = item.get("sku", "")
            category = categorize(sku)
            net_cents = int(item.get("totalPriceCents", 0)) - int(item.get("discountCents", 0))
            by_month[month][category] += net_cents
            if category == "Other" and sku:
                unmapped[month].add(sku)

    return by_month, unmapped


def print_table(by_month: dict[str, dict[str, int]], since: date, until: date) -> None:
    months = sorted(by_month.keys(), reverse=True)
    if not months:
        print("No invoices found in the period.")
        return

    drop_other = all(by_month[m].get("Other", 0) == 0 for m in months)
    columns = [c for c in CATEGORY_ORDER if c != "Other" or not drop_other]

    header_cells = [f"{'Month':<7}", f"{'Total':>10}"] + [f"{c:>18}" for c in columns]
    header = "  ".join(header_cells)
    print(f"Expenses from {since.strftime('%Y-%m')} through {until.strftime('%Y-%m')}.")
    print(header)
    print("-" * len(header))

    for month in months:
        row = by_month[month]
        total = sum(row.values()) / 100
        cells = [f"{month:<7}", f"${total:>9,.2f}"]
        for col in columns:
            cells.append(f"${row.get(col, 0) / 100:>17,.2f}")
        print("  ".join(cells))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Output JSON instead of a table.")
    parser.add_argument(
        "--show-unmapped",
        action="store_true",
        help="List SKUs that fell into the 'Other' bucket.",
    )
    args = parser.parse_args()

    base_url = env("MONGODB_ATLAS_BASE_URL").rstrip("/")
    client_id = env("MONGODB_ATLAS_CLIENT_ID")
    client_secret = env("MONGODB_ATLAS_CLIENT_SECRET")
    org_id = env("MONGODB_ATLAS_ORG_ID")

    today = datetime.now(timezone.utc).date()
    until = today.replace(day=1)
    since = until
    for _ in range(11):
        since = (since - timedelta(days=1)).replace(day=1)

    token = get_access_token(base_url, client_id, client_secret)
    invoices = list_invoices(base_url, org_id, token, since)
    detailed = [fetch_invoice(base_url, org_id, token, inv["id"]) for inv in invoices]
    by_month, unmapped = build_matrix(detailed)

    if args.json:
        payload = {
            "since": since.isoformat(),
            "until": until.isoformat(),
            "months": {
                m: {c: round(v / 100, 2) for c, v in cats.items()}
                for m, cats in sorted(by_month.items(), reverse=True)
            },
        }
        if args.show_unmapped:
            payload["unmapped_skus"] = {m: sorted(s) for m, s in sorted(unmapped.items())}
        print(json.dumps(payload, indent=2))
        return

    print_table(by_month, since, today.replace(day=1) - timedelta(days=1))
    if args.show_unmapped and unmapped:
        print()
        print("Unmapped SKUs (bucketed as 'Other'):")
        for month, skus in sorted(unmapped.items()):
            print(f"  {month}: {', '.join(sorted(skus))}")


if __name__ == "__main__":
    main()
