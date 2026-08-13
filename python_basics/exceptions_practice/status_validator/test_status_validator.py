import unittest

from status_validator import InvalidStatusError, validate_status


class StatusValidatorTests(unittest.TestCase):
    def test_returns_normalized_valid_status(self):
        result = validate_status(" NEW ")

        self.assertEqual(result, "new")

    def test_accepts_default_allowed_statuses(self):
        self.assertEqual(validate_status("in_progress"), "in_progress")
        self.assertEqual(validate_status("done"), "done")

    def test_raises_error_for_invalid_status(self):
        with self.assertRaises(InvalidStatusError):
            validate_status("cancelled")

    def test_accepts_custom_allowed_statuses(self):
        result = validate_status("active", allowed_statuses={"active", "inactive"})

        self.assertEqual(result, "active")

    def test_custom_error_is_value_error(self):
        self.assertTrue(issubclass(InvalidStatusError, ValueError))


if __name__ == "__main__":
    unittest.main()
