#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2.32",
# ]
# ///
"""Show the last 12 months of expenses for a MongoDB Atlas organization.

Authenticates with an Atlas Service Account via OAuth2 client credentials.
Reads configuration from environment variables:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET
    MONGODB_ATLAS_BASE_URL    (e.g. https://cloud.mongodb.com)
    MONGODB_ATLAS_ORG_ID

Usage:
    uv run atlas_expenses.py [--json]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, datetime, timedelta, timezone

import requests

API_VERSION = "application/vnd.atlas.2023-01-01+json"
PAGE_SIZE = 100


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


def fetch_invoices(base_url: str, org_id: str, token: str, since: date) -> list[dict]:
    invoices: list[dict] = []
    page = 1
    headers = {
        "Accept": API_VERSION,
        "Authorization": f"Bearer {token}",
    }
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

    return invoices


def parse_date(value: str) -> date:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).date()


def to_rows(invoices: list[dict], since: date) -> list[dict]:
    rows = []
    for inv in invoices:
        start = parse_date(inv["startDate"])
        if start < since:
            continue
        rows.append(
            {
                "invoice_id": inv.get("id", ""),
                "period": start.strftime("%Y-%m"),
                "status": inv.get("statusName", "UNKNOWN"),
                "subtotal_usd": round(int(inv.get("subtotalCents", 0)) / 100, 2),
                "tax_usd": round(int(inv.get("salesTaxCents", 0)) / 100, 2),
                "billed_usd": round(int(inv.get("amountBilledCents", 0)) / 100, 2),
                "paid_usd": round(int(inv.get("amountPaidCents", 0)) / 100, 2),
                "start_date": start.isoformat(),
            }
        )
    rows.sort(key=lambda r: r["start_date"], reverse=True)
    return rows


def print_table(rows: list[dict]) -> None:
    if not rows:
        print("No invoices found in the last 12 months.")
        return

    header = (
        f"{'Invoice ID':<26}  {'Period':<7}  {'Status':<10}  "
        f"{'Subtotal':>12}  {'Tax':>10}  {'Billed':>12}  {'Paid':>12}"
    )
    print(header)
    print("-" * len(header))
    sub_total = tax_total = billed_total = paid_total = 0.0
    for row in rows:
        sub_total += row["subtotal_usd"]
        tax_total += row["tax_usd"]
        billed_total += row["billed_usd"]
        paid_total += row["paid_usd"]
        print(
            f"{row['invoice_id']:<26}  {row['period']:<7}  {row['status']:<10}  "
            f"{row['subtotal_usd']:>12,.2f}  {row['tax_usd']:>10,.2f}  "
            f"{row['billed_usd']:>12,.2f}  {row['paid_usd']:>12,.2f}"
        )
    print("-" * len(header))
    print(
        f"{'Total':<26}  {'':<7}  {'':<10}  "
        f"{sub_total:>12,.2f}  {tax_total:>10,.2f}  "
        f"{billed_total:>12,.2f}  {paid_total:>12,.2f}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Output JSON instead of a table.")
    args = parser.parse_args()

    base_url = env("MONGODB_ATLAS_BASE_URL").rstrip("/")
    client_id = env("MONGODB_ATLAS_CLIENT_ID")
    client_secret = env("MONGODB_ATLAS_CLIENT_SECRET")
    org_id = env("MONGODB_ATLAS_ORG_ID")

    today = datetime.now(timezone.utc).date()
    since = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
    for _ in range(11):
        since = (since - timedelta(days=1)).replace(day=1)

    token = get_access_token(base_url, client_id, client_secret)
    invoices = fetch_invoices(base_url, org_id, token, since)
    rows = to_rows(invoices, since)

    if args.json:
        print(json.dumps({"since": since.isoformat(), "invoices": rows}, indent=2))
    else:
        print(f"MongoDB Atlas expenses since {since.isoformat()} (org {org_id})")
        print()
        print_table(rows)


if __name__ == "__main__":
    main()
