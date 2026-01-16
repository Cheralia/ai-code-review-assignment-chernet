import unittest
from correct_task3 import average_valid_measurements

class TestAverageValidMeasurements(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(average_valid_measurements([]), 0.0)

    def test_all_none_values(self):
        self.assertEqual(average_valid_measurements([None, None, None]), 0.0)

    def test_all_valid_numbers(self):
        values = [1, 2, 3, 4]
        self.assertEqual(average_valid_measurements(values), 2.5)

    def test_mixed_valid_and_none(self):
        values = [1, None, 3]
        self.assertEqual(average_valid_measurements(values), 2.0)

    def test_string_numbers(self):
        values = ["1", "2.5", "3"]
        self.assertAlmostEqual(average_valid_measurements(values), 2.1666666666666665)

    def test_invalid_values_skipped(self):
        values = [1, "abc", None, {}, [], 3]
        self.assertEqual(average_valid_measurements(values), 2.0)

    def test_negative_and_zero_values(self):
        values = [0, -1, 1]
        self.assertEqual(average_valid_measurements(values), 0.0)

if __name__ == "__main__":
    unittest.main()
