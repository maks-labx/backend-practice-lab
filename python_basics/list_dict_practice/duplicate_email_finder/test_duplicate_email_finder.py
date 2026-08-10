import unittest

from duplicate_email_finder import find_duplicate_emails


class DuplicateEmailFinderTests(unittest.TestCase):
    def test_finds_duplicate_emails(self):
        emails = [
            "max@example.com",
            "anna@example.com",
            "max@example.com",
        ]

        result = find_duplicate_emails(emails)

        self.assertEqual(result, ["max@example.com"])

    def test_detects_duplicates_with_different_case_and_spaces(self):
        emails = [
            "Max@Example.com",
            "anna@example.com",
            " max@example.com ",
            "ANNA@example.com",
        ]

        result = find_duplicate_emails(emails)

        self.assertEqual(result, ["anna@example.com", "max@example.com"])

    def test_returns_empty_list_when_no_duplicates(self):
        emails = [
            "max@example.com",
            "anna@example.com",
            "john@example.com",
        ]

        result = find_duplicate_emails(emails)

        self.assertEqual(result, [])

    def test_ignores_empty_emails(self):
        emails = [
            "",
            "   ",
            "max@example.com",
            "MAX@example.com",
        ]

        result = find_duplicate_emails(emails)

        self.assertEqual(result, ["max@example.com"])


if __name__ == "__main__":
    unittest.main()
