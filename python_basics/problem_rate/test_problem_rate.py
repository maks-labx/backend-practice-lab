import unittest

from problem_rate import calculate_problem_rate


class CalculateProblemRateTests(unittest.TestCase):
    def test_returns_50_when_half_statuses_are_problems(self):
        statuses = ["OK", "PROBLEM", "OK", "PROBLEM"]

        result = calculate_problem_rate(statuses)

        self.assertEqual(result, 50.0)

    def test_returns_0_when_no_problems(self):
        statuses = ["OK", "OK", "OK"]

        result = calculate_problem_rate(statuses)

        self.assertEqual(result, 0.0)

    def test_returns_100_when_all_are_problems(self):
        statuses = ["PROBLEM", "PROBLEM"]

        result = calculate_problem_rate(statuses)

        self.assertEqual(result, 100.0)

    def test_returns_0_for_empty_list(self):
        result = calculate_problem_rate([])

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()