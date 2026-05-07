"""Fetch and display the latest 12 Atlas invoices.

Mirrors atlas-sdk-go/examples/invoice/invoice.go. Demonstrates the Billing API.

Required env vars:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET
"""

import datetime as dt
from typing import Any

from _atlas import get_client, get_org_id


def list_latest_invoices(client: Any, org_id: str) -> list[Any]:
    """Fetch the latest invoice metadata page."""
    page = client.invoices.list_invoices(org_id=org_id, items_per_page=12, page_num=1)
    return page.results or []


def invoice_rows(invoices: list[Any]) -> list[dict[str, str]]:
    """Return printable table rows for invoice metadata."""
    return [
        {
            "id": invoice.id or "-",
            "status": invoice.status_name or "-",
            "created": _date(invoice.created),
            "period": _period(invoice.start_date, invoice.end_date),
            "subtotal": _money(invoice.subtotal_cents or 0),
            "tax": _money(invoice.sales_tax_cents or 0),
            "billed": _money(invoice.amount_billed_cents or 0),
            "paid": _money(invoice.amount_paid_cents or 0),
        }
        for invoice in invoices
    ]


def main() -> None:
    client = get_client()
    org_id = get_org_id(client)

    invoices = list_latest_invoices(client, org_id)
    if not invoices:
        print("No invoices found.")
        return

    rows = invoice_rows(invoices)
    _print_table(rows)


def _print_table(rows: list[dict[str, str]]) -> None:
    headers = {
        "id": "Invoice ID",
        "status": "Status",
        "created": "Created",
        "period": "Period",
        "subtotal": "Subtotal",
        "tax": "Tax",
        "billed": "Billed",
        "paid": "Paid",
    }
    widths = {
        key: max(len(label), *(len(row[key]) for row in rows))
        for key, label in headers.items()
    }
    header = (
        f"{headers['id']:<{widths['id']}}  "
        f"{headers['status']:<{widths['status']}}  "
        f"{headers['created']:<{widths['created']}}  "
        f"{headers['period']:<{widths['period']}}  "
        f"{headers['subtotal']:>{widths['subtotal']}}  "
        f"{headers['tax']:>{widths['tax']}}  "
        f"{headers['billed']:>{widths['billed']}}  "
        f"{headers['paid']:>{widths['paid']}}"
    )
    print(header)
    print("-" * len(header))
    for row in rows:
        print(
            f"{row['id']:<{widths['id']}}  "
            f"{row['status']:<{widths['status']}}  "
            f"{row['created']:<{widths['created']}}  "
            f"{row['period']:<{widths['period']}}  "
            f"{row['subtotal']:>{widths['subtotal']}}  "
            f"{row['tax']:>{widths['tax']}}  "
            f"{row['billed']:>{widths['billed']}}  "
            f"{row['paid']:>{widths['paid']}}"
        )


def _date(value: dt.datetime | None) -> str:
    if value is None:
        return "-"
    return value.date().isoformat()


def _period(start: dt.datetime | None, end: dt.datetime | None) -> str:
    if start is None or end is None:
        return "-"
    return f"{start.date().isoformat()} to {end.date().isoformat()}"


def _money(cents: int) -> str:
    return f"${cents / 100:,.2f}"


if __name__ == "__main__":
    main()
