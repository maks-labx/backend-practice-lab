import unittest
from datetime import date 

from overdue_checker import is_overdue

class IsOverdueTests(unittest.TestCase):
    def test_due_date_before_today_is_overdue(self):
        due_date = date(2026, 6, 18)
        today = date(2026, 6, 20)

        result = is_overdue(due_date, today)

        self.assertTrue(result)

    def test_due_date_equal_today_is_not_overdue(self):
        due_date = date(2026, 6, 20)
        today = date(2026, 6, 20)

        result = is_overdue(due_date, today)

        self.assertFalse(result)

    def test_due_date_after_today_is_not_overdue(self):
        due_date = date(2026, 6, 22)
        today = date(2026, 6, 20)

        result = is_overdue(due_date, today)

        self.assertFalse(result)

if __name__=="__main__":
    unittest.main()