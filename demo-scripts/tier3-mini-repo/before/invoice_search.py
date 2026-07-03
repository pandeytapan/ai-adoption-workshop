"""Invoice search for the distributor portal.

Existing, working reference implementation for how search/listing endpoints
in this codebase page results. order_search.py was added later by a
different contributor and does not follow this pattern (see its bug).
"""

from dataclasses import dataclass

from pagination import total_pages


@dataclass
class Invoice:
    invoice_id: str
    customer_id: str
    amount_cents: int


def search_invoices(invoices, customer_id, page=1, page_size=100):
    """Return one page of invoices for a customer, oldest invoice_id first."""
    matches = sorted(
        (i for i in invoices if i.customer_id == customer_id),
        key=lambda i: i.invoice_id,
    )

    pages = total_pages(len(matches), page_size)
    if page > pages:
        return []

    start = (page - 1) * page_size
    end = start + page_size
    return matches[start:end]
