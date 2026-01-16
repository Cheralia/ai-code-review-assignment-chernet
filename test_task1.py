import unittest
from correct_task1 import calculate_average_order_value

class TestCalculateAverageOrderValue(unittest.TestCase):

    def test_empty_orders(self):
        self.assertEqual(calculate_average_order_value([]), 0.0)

    def test_all_cancelled_orders(self):
        orders = [
            {"status": "cancelled", "amount": 100},
            {"status": "cancelled", "amount": 200},
        ]
        self.assertEqual(calculate_average_order_value(orders), 0.0)

    def test_mixed_orders(self):
        orders = [
            {"status": "completed", "amount": 100},
            {"status": "cancelled", "amount": 200},
            {"status": "completed", "amount": 300},
        ]
        self.assertEqual(calculate_average_order_value(orders), 200.0)

    def test_missing_status_key(self):
        orders = [
            {"amount": 100},
            {"status": "cancelled", "amount": 200},
        ]
        self.assertEqual(calculate_average_order_value(orders), 100.0)

    def test_invalid_amount_values(self):
        orders = [
            {"status": "completed", "amount": "100"},
            {"status": "completed", "amount": "abc"},
            {"status": "completed", "amount": None},
        ]
        self.assertEqual(calculate_average_order_value(orders), 100.0)

    def test_float_amounts(self):
        orders = [
            {"status": "completed", "amount": 99.5},
            {"status": "completed", "amount": 100.5},
        ]
        self.assertEqual(calculate_average_order_value(orders), 100.0)

if __name__ == "__main__":
    unittest.main()
