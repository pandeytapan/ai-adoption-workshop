# Tier 3 demo materials — "Fix a failing test"

This is the concrete, downloadable example behind Tier 3's live demo slides.
It continues the Meridian Industrial Supply story from Tiers 1 and 2: this is
a small slice of the actual distributor-portal codebase being built for
Meridian, and the bug below is one Northbridge's engineers hit while
implementing RFP requirement #6 ("search that doesn't crawl once we're past
10k records" — see `../sample-rfp-distributor-portal.md`).

## The scenario

`before/order_search.py` has a genuine, subtle bug: it reimplements
page-count math locally using floor division (`len(matches) // page_size`)
instead of using the project's existing shared helper,
`pagination.total_pages()` — which `before/invoice_search.py` already uses
correctly.

The bug only shows up when a customer's total order count is **not** an
exact multiple of the page size. Hendricks Supply, the high-volume API
customer named in RFP requirement #9, has 10,050 open orders — so their
final page of 50 orders silently disappears from search entirely.
`before/test_order_search.py` encodes this as a real, runnable, genuinely
failing test.

## The live prompt used

> "This test is failing. Find out why, fix the underlying issue (not just
> the test), and show me what you changed and why before you commit
> anything."

(This is Option A from `../tier3-coding-agent.md`.)

## What actually happened (this was run for real, not simulated)

1. Ran `pytest before/test_order_search.py` — confirmed
   `test_search_orders_returns_final_partial_page` genuinely fails
   (`0 == 50`), while the exact-multiple regression test already passes.
2. Read `order_search.py` — found a comment flagging that page-count math
   was reimplemented locally instead of using the project's shared helper.
3. Read `invoice_search.py` and `pagination.py` — found the existing,
   correct convention already used elsewhere in the codebase
   (`pagination.total_pages()`, which rounds up).
4. Fixed `order_search.py` to import and use `pagination.total_pages()`
   instead of patching the floor-division bug in isolation — the fix
   follows the codebase's existing convention rather than adding a second,
   slightly different way to do the same thing.
5. Re-ran the tests — both pass. See `order_search.diff` for the exact
   change (net: +3 lines, -3 lines).

## Files here

| File | What it is |
|---|---|
| `before/order_search.py` | The buggy module, as it existed when the test was failing |
| `before/pagination.py` | The project's existing, correct shared pagination helper |
| `before/invoice_search.py` | An existing module that already uses the helper correctly |
| `before/test_order_search.py` | The real, runnable failing test |
| `after/order_search.py` | The fixed module |
| `order_search.diff` | Unified diff of the actual fix |
