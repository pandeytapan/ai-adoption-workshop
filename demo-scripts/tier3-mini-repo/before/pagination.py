"""Shared pagination utilities used across the distributor portal backend.

Every search/listing endpoint in this codebase is expected to use
total_pages() below rather than reimplementing page-count math locally.
See invoice_search.py for the reference usage pattern.
"""

import math


def total_pages(total_matches: int, page_size: int) -> int:
    """Return the number of pages needed to cover total_matches results.

    Always rounds up, so a partial final page still counts as a page.
    """
    if page_size <= 0:
        raise ValueError("page_size must be positive")
    if total_matches <= 0:
        return 0
    return math.ceil(total_matches / page_size)
