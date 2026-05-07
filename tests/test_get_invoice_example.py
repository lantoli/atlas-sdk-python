import datetime as dt
import os
import sys
from types import SimpleNamespace

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "examples"))

from get_invoice import invoice_rows, list_latest_invoices


def test_list_latest_invoices_fetches_first_page_with_12_items():
    calls = []

    class FakeInvoices:
        def list_invoices(self, **kwargs):
            calls.append(kwargs)
            return SimpleNamespace(results=[SimpleNamespace(id="invoice-1")])

    invoices = list_latest_invoices(SimpleNamespace(invoices=FakeInvoices()), "org-id")

    assert [invoice.id for invoice in invoices] == ["invoice-1"]
    assert calls == [
        {
            "org_id": "org-id",
            "items_per_page": 12,
            "page_num": 1,
        }
    ]


def test_invoice_rows_formats_latest_invoice_table_rows():
    rows = invoice_rows(
        [
            SimpleNamespace(
                id="invoice-1",
                status_name="PAID",
                created=dt.datetime(2026, 5, 2, 3, 4, 5),
                start_date=dt.datetime(2026, 4, 1),
                end_date=dt.datetime(2026, 5, 1),
                subtotal_cents=10000,
                sales_tax_cents=2345,
                amount_billed_cents=12345,
                amount_paid_cents=12000,
            ),
            SimpleNamespace(
                id="invoice-2",
                status_name=None,
                created=None,
                start_date=None,
                end_date=None,
                subtotal_cents=None,
                sales_tax_cents=None,
                amount_billed_cents=None,
                amount_paid_cents=None,
            ),
        ]
    )

    assert rows == [
        {
            "id": "invoice-1",
            "status": "PAID",
            "created": "2026-05-02",
            "period": "2026-04-01 to 2026-05-01",
            "subtotal": "$100.00",
            "tax": "$23.45",
            "billed": "$123.45",
            "paid": "$120.00",
        },
        {
            "id": "invoice-2",
            "status": "-",
            "created": "-",
            "period": "-",
            "subtotal": "$0.00",
            "tax": "$0.00",
            "billed": "$0.00",
            "paid": "$0.00",
        },
    ]
