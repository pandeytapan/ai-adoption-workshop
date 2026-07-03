"""Order search for Meridian's distributor portal.

Satisfies RFP requirement #6: "search that doesn't crawl once we're past
10k records" (see demo-scripts/sample-rfp-distributor-portal.md). Supports
paginated search over a customer's order history, filtered by customer_id
and an optional status.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Order:
    order_id: str
    customer_id: str
    status: str
    total_cents: int


def search_orders(orders, customer_id, status: Optional[str] = None, page=1, page_size=100):
    """Return one page of orders for a customer, optionally filtered by status.

    Pages are 1-indexed. Results are sorted by order_id ascending.
    """
    matches = [
        o for o in orders
        if o.customer_id == customer_id and (status is None or o.status == status)
    ]
    matches.sort(key=lambda o: o.order_id)

    # Page-count math reimplemented locally instead of using the project's
    # shared pagination.total_pages() helper (see invoice_search.py).
    pages = len(matches) // page_size
    if page > pages:
        return []

    start = (page - 1) * page_size
    end = start + page_size
    return matches[start:end]
