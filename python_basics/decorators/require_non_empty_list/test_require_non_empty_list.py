import unittest

from require_non_empty_list import calculate_total


class RequireNonEmptyListTests(unittest.TestCase):
    def test_returns_sum_for_non_empty_list(self):
        result = calculate_total([10, 20, 30])

        self.assertEqual(result, 60)

    def test_returns_0_for_empty_list(self):
        result = calculate_total([])

        self.assertEqual(result, 0)

    def test_returns_0_for_none(self):
        result = calculate_total(None)

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()