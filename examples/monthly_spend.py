"""Show monthly Atlas spend by service family for the last 12 months.

Uses invoice line items and rolls Atlas SKU names into readable service-family
columns.

Required env vars:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET
"""

import datetime as dt
from collections import defaultdict
from typing import Any

from _atlas import get_client, get_org_id


def last_12_month_window(today: dt.date | None = None) -> tuple[dt.date, dt.date]:
    """Return a calendar-month window covering the current month and prior 11 months."""
    today = today or dt.date.today()
    current_month = today.replace(day=1)
    return _add_months(current_month, -11), _add_months(current_month, 1)


def list_recent_invoices(client: Any, org_id: str, *, today: dt.date | None = None) -> list[Any]:
    """Fetch invoices whose billing periods overlap the last 12 calendar months."""
    from_date, to_date = last_12_month_window(today)
    invoices: list[Any] = []
    page = 1
    while True:
        response = client.invoices.list_invoices(
            org_id=org_id,
            items_per_page=100,
            page_num=page,
            from_date=from_date,
            to_date=to_date,
        )
        page_invoices = response.results or []
        invoices.extend(page_invoices)
        if len(page_invoices) < 100:
            return invoices
        page += 1


def list_recent_invoice_details(client: Any, org_id: str, *, today: dt.date | None = None) -> list[Any]:
    """Fetch detailed invoices for the last 12 calendar months."""
    return invoice_details(client, org_id, list_recent_invoices(client, org_id, today=today))


def invoice_details(client: Any, org_id: str, invoices: list[Any]) -> list[Any]:
    """Fetch detailed invoice records for invoice metadata rows."""
    details = []
    for invoice in invoices:
        if invoice.id is None:
            continue
        details.append(client.invoices.get_invoice(org_id, invoice.id))
    return details


def aggregate_monthly_service_spend(
    invoices: list[Any],
    *,
    start_month: dt.date,
    end_month: dt.date,
) -> dict[str, dict[str, int]]:
    """Group detailed invoice line items by month and readable service family."""
    monthly: dict[str, dict[str, int]] = {
        month.strftime("%Y-%m"): defaultdict(int) for month in _month_range(start_month, end_month)
    }
    for invoice in invoices:
        month_date = _invoice_month(invoice)
        if month_date is None or month_date < start_month or month_date >= end_month:
            continue

        month = month_date.strftime("%Y-%m")
        for line_item in invoice.line_items or []:
            monthly[month][service_label(line_item.sku or line_item.note)] += line_item.total_price_cents or 0
    return {month: dict(services) for month, services in monthly.items()}


def monthly_service_spend_rows(
    monthly: dict[str, dict[str, int]],
) -> tuple[list[dict[str, str]], list[str]]:
    """Return printable service pivot rows and the ordered service columns."""
    services = _services_with_spend(monthly)
    rows: list[dict[str, str]] = []
    for month in sorted(monthly, reverse=True):
        service_amounts = monthly[month]
        row = {
            "month": month,
            "total": _money(sum(service_amounts.values())),
        }
        for service in services:
            row[service] = _money(service_amounts.get(service, 0))
        rows.append(row)
    return rows, services


def main() -> None:
    client = get_client()
    org_id = get_org_id(client)
    from_date, to_date = last_12_month_window()
    invoices = list_recent_invoices(client, org_id)
    detailed_invoices = invoice_details(client, org_id, invoices)
    monthly_services = aggregate_monthly_service_spend(
        detailed_invoices,
        start_month=from_date,
        end_month=to_date,
    )

    if not invoices:
        print("No invoices found for the last 12 months.")
        return

    rows, services = monthly_service_spend_rows(monthly_services)
    if not services:
        print("No invoice line items found for the last 12 months.")
        return

    print(f"Expenses from {from_date:%Y-%m} through {(to_date - dt.timedelta(days=1)):%Y-%m}.")
    _print_table(rows, services)


def service_label(value: str | None) -> str:
    """Return a compact service family label for an invoice SKU or note."""
    if not value:
        return "Unknown"

    tokens = [token for token in value.upper().replace("-", "_").split("_") if token]
    product_tokens = [token for token in tokens if token not in {"ATLAS", "AWS", "AZURE", "GCP"}]

    if "STREAM" in product_tokens and "PROCESSING" in product_tokens:
        return "Stream Processing"
    if "SEARCH" in product_tokens:
        return "Atlas Search"
    if "DATA" in product_tokens and "TRANSFER" in product_tokens:
        return "Data Transfer"
    if "PRIVATE" in product_tokens and "ENDPOINT" in product_tokens:
        return "Private Endpoint"
    if "STORAGE" in product_tokens or "IOPS" in product_tokens:
        return "Storage"
    if "BACKUP" in product_tokens or "SNAPSHOT" in product_tokens:
        return "Backup"
    if "INSTANCE" in product_tokens or "FLEX" in product_tokens:
        return "Clusters"
    if "BI" in product_tokens and "CONNECTOR" in product_tokens:
        return "BI Connector"
    if "AUDITING" in product_tokens:
        return "Auditing"
    if "SECURITY" in product_tokens:
        return "Advanced Security"

    return _title_label(product_tokens or tokens)


def _invoice_month(invoice: Any) -> dt.date | None:
    invoice_date = invoice.start_date or invoice.created
    if invoice_date is None:
        return None
    return dt.date(invoice_date.year, invoice_date.month, 1)


def _title_label(tokens: list[str]) -> str:
    words = []
    for token in tokens:
        if token in {"BI", "IOPS", "VPC"}:
            words.append(token)
        elif token:
            words.append(token.title())
    return " ".join(words) or "Unknown"


def _print_table(rows: list[dict[str, str]], services: list[str]) -> None:
    widths = {
        "month": max(len("Month"), *(len(row["month"]) for row in rows)),
        "total": max(len("Total"), *(len(row["total"]) for row in rows)),
        **{
            service: max(len(service), *(len(row[service]) for row in rows))
            for service in services
        },
    }
    header = f"{'Month':<{widths['month']}}  {'Total':>{widths['total']}}"
    for service in services:
        header = f"{header}  {service:>{widths[service]}}"
    print(header)
    print("-" * len(header))
    for row in rows:
        line = f"{row['month']:<{widths['month']}}  {row['total']:>{widths['total']}}"
        for service in services:
            line = f"{line}  {row[service]:>{widths[service]}}"
        print(line)


def _money(cents: int) -> str:
    return f"${cents / 100:,.2f}"


def _services_with_spend(monthly: dict[str, dict[str, int]]) -> list[str]:
    service_totals: defaultdict[str, int] = defaultdict(int)
    for service_amounts in monthly.values():
        for service, amount in service_amounts.items():
            service_totals[service] += amount
    return [
        service
        for service, amount in sorted(
            service_totals.items(),
            key=lambda item: (-item[1], item[0]),
        )
        if amount
    ]


def _add_months(value: dt.date, months: int) -> dt.date:
    month_index = value.year * 12 + value.month - 1 + months
    return dt.date(month_index // 12, month_index % 12 + 1, 1)


def _month_range(start_month: dt.date, end_month: dt.date) -> list[dt.date]:
    months = []
    month = start_month
    while month < end_month:
        months.append(month)
        month = _add_months(month, 1)
    return months


if __name__ == "__main__":
    main()
