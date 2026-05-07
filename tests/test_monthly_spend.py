import datetime as dt
import os
import sys
from types import SimpleNamespace

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "examples"))

from monthly_spend import (
    aggregate_monthly_service_spend,
    invoice_details,
    last_12_month_window,
    list_recent_invoices,
    monthly_service_spend_rows,
    service_label,
)


def test_last_12_month_window_includes_current_month():
    assert last_12_month_window(dt.date(2026, 5, 12)) == (
        dt.date(2025, 6, 1),
        dt.date(2026, 6, 1),
    )


def test_list_recent_invoices_uses_date_filters_without_sorting_params():
    calls = []

    class FakeInvoices:
        def list_invoices(self, **kwargs):
            calls.append(kwargs)
            return SimpleNamespace(results=[])

    invoices = list_recent_invoices(
        SimpleNamespace(invoices=FakeInvoices()),
        "org-id",
        today=dt.date(2026, 5, 12),
    )

    assert invoices == []
    assert calls == [
        {
            "org_id": "org-id",
            "items_per_page": 100,
            "page_num": 1,
            "from_date": dt.date(2025, 6, 1),
            "to_date": dt.date(2026, 6, 1),
        }
    ]


def test_monthly_service_spend_rows_pivot_services_by_month():
    invoices = [
        SimpleNamespace(
            start_date=dt.datetime(2025, 6, 1),
            created=dt.datetime(2025, 6, 15),
            line_items=[
                SimpleNamespace(sku="ATLAS_AWS_INSTANCE_M10", note=None, total_price_cents=260),
                SimpleNamespace(sku="ATLAS_AWS_STORAGE_IOPS", note=None, total_price_cents=40),
            ],
        ),
        SimpleNamespace(
            start_date=dt.datetime(2025, 7, 1),
            created=dt.datetime(2025, 7, 15),
            line_items=[
                SimpleNamespace(sku="ATLAS_AWS_DATA_TRANSFER_INTERNET", note=None, total_price_cents=50),
            ],
        ),
    ]

    monthly = aggregate_monthly_service_spend(
        invoices,
        start_month=dt.date(2025, 6, 1),
        end_month=dt.date(2025, 8, 1),
    )
    rows, services = monthly_service_spend_rows(monthly)

    assert services == ["Clusters", "Data Transfer", "Storage"]
    assert rows == [
        {
            "month": "2025-07",
            "total": "$0.50",
            "Clusters": "$0.00",
            "Storage": "$0.00",
            "Data Transfer": "$0.50",
        },
        {
            "month": "2025-06",
            "total": "$3.00",
            "Clusters": "$2.60",
            "Storage": "$0.40",
            "Data Transfer": "$0.00",
        },
    ]


def test_service_label_groups_raw_skus_into_readable_columns():
    assert service_label("ATLAS_AWS_INSTANCE_M10") == "Clusters"
    assert service_label("ATLAS_AWS_PRIVATE_ENDPOINT") == "Private Endpoint"
    assert service_label("ATLAS_AWS_STORAGE_IOPS") == "Storage"
    assert service_label("ATLAS_AWS_DATA_TRANSFER_INTERNET") == "Data Transfer"
    assert service_label("ATLAS_AWS_SEARCH_INSTANCE_S20_COMPUTE_NVME") == "Atlas Search"
    assert service_label("ATLAS_AWS_STREAM_PROCESSING_INSTANCE_SP30") == "Stream Processing"
    assert service_label("ATLAS_BI_CONNECTOR") == "BI Connector"
    assert service_label("ATLAS_ADVANCED_SECURITY") == "Advanced Security"


def test_monthly_service_spend_uses_note_when_sku_is_missing():
    invoices = [
        SimpleNamespace(
            start_date=dt.datetime(2025, 6, 1),
            created=dt.datetime(2025, 6, 15),
            line_items=[
                SimpleNamespace(sku=None, note="Support", total_price_cents=100),
            ],
        )
    ]

    monthly = aggregate_monthly_service_spend(
        invoices,
        start_month=dt.date(2025, 6, 1),
        end_month=dt.date(2025, 7, 1),
    )

    assert monthly == {"2025-06": {"Support": 100}}


def test_invoice_details_fetches_each_invoice_by_id():
    calls = []

    class FakeInvoices:
        def get_invoice(self, org_id, invoice_id):
            calls.append((org_id, invoice_id))
            return SimpleNamespace(id=invoice_id)

    details = invoice_details(
        SimpleNamespace(invoices=FakeInvoices()),
        "org-id",
        [SimpleNamespace(id="invoice-1"), SimpleNamespace(id=None), SimpleNamespace(id="invoice-2")],
    )

    assert [invoice.id for invoice in details] == ["invoice-1", "invoice-2"]
    assert calls == [("org-id", "invoice-1"), ("org-id", "invoice-2")]
