def average_valid_measurements(values):
    """
    Calculate the average of valid (non-None, numeric) measurements.

    Args:
        values (list): A list of values that may include None or non-numeric types.

    Returns:
        float: The average of valid numeric values, or 0.0 if none exist.
    """
    total = 0.0
    valid_count = 0

    for v in values:
        if v is not None:
            try:
                total += float(v)
                valid_count += 1
            except (TypeError, ValueError):
                continue

    if valid_count == 0:
        return 0.0

    return total / valid_count
