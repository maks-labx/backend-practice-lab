import unittest

from square_calculator import calculate_square, calculate_squares_in_processes


class SquareCalculatorTests(unittest.TestCase):
    def test_calculate_square_returns_square_of_number(self):
        result = calculate_square(5)

        self.assertEqual(result, 25)

    def test_calculate_squares_in_processes_returns_squares(self):
        numbers = [1, 2, 3, 4]

        result = calculate_squares_in_processes(numbers, max_workers=2)

        self.assertEqual(result, [1, 4, 9, 16])

    def test_preserves_input_order(self):
        numbers = [5, 1, 4, 2]

        result = calculate_squares_in_processes(numbers, max_workers=2)

        self.assertEqual(result, [25, 1, 16, 4])

    def test_handles_duplicate_numbers(self):
        numbers = [2, 2, 3]

        result = calculate_squares_in_processes(numbers, max_workers=2)

        self.assertEqual(result, [4, 4, 9])

    def test_empty_list_returns_empty_list(self):
        result = calculate_squares_in_processes([])

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
