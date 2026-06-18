import unittest

from status_counter import count_statuses

class CountStatusesTests(unittest.TestCase):
    def test_counts_multiple_statuses(self):
        statuses = ["OK", "PROBLEM", "OK", "PROBLEM", "OK"]

        result = count_statuses(statuses)

        self.assertEqual(result, {"OK": 3, "PROBLEM": 2})

    def test_empty_list_returns_empty_dict(self):
        result = count_statuses([])

        self.assertEqual(result, {})

    def test_single_status(self):
        statuses = ["OK"]

        result = count_statuses(statuses)

        self.assertEqual(result, {"OK": 1})

if __name__ == "__main__":
    unittest.main()