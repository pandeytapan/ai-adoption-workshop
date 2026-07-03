from order_search import Order, search_orders


def make_orders(customer_id, count):
    return [
        Order(order_id=f"ORD-{i:06d}", customer_id=customer_id, status="open", total_cents=1000)
        for i in range(count)
    ]


def test_search_orders_returns_final_partial_page():
    """Hendricks Supply is a high-volume API customer (RFP requirement #9)
    with 10,050 open orders. The last page (the final 50 records) must
    still be reachable through search, not silently dropped.
    """
    orders = make_orders("hendricks-supply", 10_050)
    page_size = 100
    last_page_number = 101  # ceil(10050 / 100)

    results = search_orders(orders, "hendricks-supply", page=last_page_number, page_size=page_size)

    assert len(results) == 50
    assert results[0].order_id == "ORD-010000"
    assert results[-1].order_id == "ORD-010049"


def test_search_orders_exact_multiple_still_works():
    """Sanity check: page counts that land on an exact multiple of
    page_size should keep working after any fix (regression guard).
    """
    orders = make_orders("meridian-hq", 200)
    results = search_orders(orders, "meridian-hq", page=2, page_size=100)
    assert len(results) == 100
    assert results[0].order_id == "ORD-000100"
