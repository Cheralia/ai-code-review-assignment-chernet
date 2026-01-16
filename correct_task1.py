def calculate_average_order_value(orders):
    """
    Calculate the average order value for non-cancelled orders.

    Args:
        orders (list): A list of dictionaries with keys "status" and "amount".

    Returns:
        float: The average amount of non-cancelled orders, or 0.0 if none exist.
    """
    total = 0.0
    valid_count = 0

    for order in orders:
        if order.get("status") != "cancelled":
            try:
                total += float(order.get("amount", 0))
                valid_count += 1
            except (TypeError, ValueError):
                continue

    if valid_count == 0:
        return 0.0

    return total / valid_count
