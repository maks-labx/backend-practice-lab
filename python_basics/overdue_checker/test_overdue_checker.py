import unittest
from datetime import date

from overdue_checker import days_until_due, get_due_status, is_overdue


class OverdueCheckerTests(unittest.TestCase):
    def test_returns_true_when_due_date_is_before_today(self):
        due_date = date(2026, 9, 1)
        today = date(2026, 9, 5)

        result = is_overdue(due_date, today)

        self.assertTrue(result)

    def test_returns_false_when_due_date_is_today(self):
        due_date = date(2026, 9, 5)
        today = date(2026, 9, 5)

        result = is_overdue(due_date, today)

        self.assertFalse(result)

    def test_returns_false_when_due_date_is_after_today(self):
        due_date = date(2026, 9, 10)
        today = date(2026, 9, 5)

        result = is_overdue(due_date, today)

        self.assertFalse(result)

    def test_get_due_status_returns_overdue(self):
        due_date = date(2026, 9, 1)
        today = date(2026, 9, 5)

        result = get_due_status(due_date, today)

        self.assertEqual(result, "overdue")

    def test_get_due_status_returns_due_today(self):
        due_date = date(2026, 9, 5)
        today = date(2026, 9, 5)

        result = get_due_status(due_date, today)

        self.assertEqual(result, "due_today")

    def test_get_due_status_returns_upcoming(self):
        due_date = date(2026, 9, 10)
        today = date(2026, 9, 5)

        result = get_due_status(due_date, today)

        self.assertEqual(result, "upcoming")

    def test_days_until_due_returns_positive_number_for_future_date(self):
        due_date = date(2026, 9, 10)
        today = date(2026, 9, 5)

        result = days_until_due(due_date, today)

        self.assertEqual(result, 5)

    def test_days_until_due_returns_zero_for_today(self):
        due_date = date(2026, 9, 5)
        today = date(2026, 9, 5)

        result = days_until_due(due_date, today)

        self.assertEqual(result, 0)

    def test_days_until_due_returns_negative_number_for_overdue_date(self):
        due_date = date(2026, 9, 1)
        today = date(2026, 9, 5)

        result = days_until_due(due_date, today)

        self.assertEqual(result, -4)

    def test_invalid_due_date_raises_error(self):
        with self.assertRaises(ValueError):
            is_overdue("2026-09-01", date(2026, 9, 5))

    def test_invalid_today_raises_error(self):
        with self.assertRaises(ValueError):
            is_overdue(date(2026, 9, 1), "2026-09-05")


if __name__ == "__main__":
    unittest.main()
