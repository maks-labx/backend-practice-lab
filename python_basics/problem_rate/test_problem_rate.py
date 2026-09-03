import unittest

from problem_rate import calculate_problem_rate, normalize_status


class ProblemRateTests(unittest.TestCase):
    def test_calculates_problem_rate_for_half_problems(self):
        statuses = ["OK", "PROBLEM", "OK", "PROBLEM"]

        result = calculate_problem_rate(statuses)

        self.assertEqual(result, 50.0)

    def test_calculates_problem_rate_when_no_problems(self):
        statuses = ["OK", "OK", "OK"]

        result = calculate_problem_rate(statuses)

        self.assertEqual(result, 0.0)

    def test_calculates_problem_rate_when_all_problems(self):
        statuses = ["PROBLEM", "PROBLEM", "PROBLEM"]

        result = calculate_problem_rate(statuses)

        self.assertEqual(result, 100.0)

    def test_empty_list_returns_zero(self):
        result = calculate_problem_rate([])

        self.assertEqual(result, 0)

    def test_normalizes_status_case_and_spaces(self):
        statuses = [" problem ", "PROBLEM", "Problem", "OK"]

        result = calculate_problem_rate(statuses)

        self.assertEqual(result, 75.0)

    def test_can_use_custom_problem_status(self):
        statuses = ["failed", "ok", "FAILED", " Failed "]

        result = calculate_problem_rate(statuses, problem_status="failed")

        self.assertEqual(result, 75.0)

    def test_rounds_result_to_two_decimal_places(self):
        statuses = ["PROBLEM", "OK", "OK"]

        result = calculate_problem_rate(statuses)

        self.assertEqual(result, 33.33)

    def test_normalize_status_returns_uppercase_stripped_status(self):
        result = normalize_status(" problem ")

        self.assertEqual(result, "PROBLEM")

    def test_non_string_status_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_problem_rate(["OK", None, "PROBLEM"])


if __name__ == "__main__":
    unittest.main()
