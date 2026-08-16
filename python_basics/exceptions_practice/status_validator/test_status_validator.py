import unittest

from status_validator import (
    DEFAULT_ALLOWED_STATUSES,
    InvalidStatusError,
    validate_status,
    validate_statuses,
)


class StatusValidatorTests(unittest.TestCase):
    def test_returns_normalized_valid_status(self):
        result = validate_status(" NEW ")

        self.assertEqual(result, "new")

    def test_accepts_default_allowed_statuses(self):
        self.assertEqual(validate_status("new"), "new")
        self.assertEqual(validate_status("in_progress"), "in_progress")
        self.assertEqual(validate_status("done"), "done")

    def test_raises_error_for_invalid_status(self):
        with self.assertRaises(InvalidStatusError):
            validate_status("cancelled")

    def test_raises_error_for_empty_status(self):
        with self.assertRaises(InvalidStatusError):
            validate_status("   ")

    def test_raises_error_for_non_string_status(self):
        with self.assertRaises(InvalidStatusError):
            validate_status(None)

        with self.assertRaises(InvalidStatusError):
            validate_status(123)

    def test_accepts_custom_allowed_statuses(self):
        result = validate_status("active", allowed_statuses={"active", "inactive"})

        self.assertEqual(result, "active")

    def test_validate_statuses_returns_normalized_statuses(self):
        result = validate_statuses([" NEW ", "DONE", "in_progress"])

        self.assertEqual(result, ["new", "done", "in_progress"])

    def test_validate_statuses_accepts_custom_allowed_statuses(self):
        result = validate_statuses(
            ["active", " INACTIVE "],
            allowed_statuses={"active", "inactive"},
        )

        self.assertEqual(result, ["active", "inactive"])

    def test_validate_statuses_raises_error_if_one_status_is_invalid(self):
        with self.assertRaises(InvalidStatusError):
            validate_statuses(["new", "cancelled", "done"])

    def test_custom_error_is_value_error(self):
        self.assertTrue(issubclass(InvalidStatusError, ValueError))

    def test_default_allowed_statuses_contains_expected_values(self):
        self.assertEqual(
            DEFAULT_ALLOWED_STATUSES,
            {"new", "in_progress", "done"},
        )


if __name__ == "__main__":
    unittest.main()
