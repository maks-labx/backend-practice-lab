import unittest
from types import GeneratorType

from sliding_window_generator import sliding_window


class SlidingWindowGeneratorTests(unittest.TestCase):
    def test_generates_windows_of_given_size(self):
        items = [1, 2, 3, 4]

        result = list(sliding_window(items, 2))

        self.assertEqual(result, [(1, 2), (2, 3), (3, 4)])

    def test_generates_windows_with_size_three(self):
        items = [1, 2, 3, 4, 5]

        result = list(sliding_window(items, 3))

        self.assertEqual(result, [(1, 2, 3), (2, 3, 4), (3, 4, 5)])

    def test_returns_empty_list_when_items_less_than_size(self):
        items = [1, 2]

        result = list(sliding_window(items, 3))

        self.assertEqual(result, [])

    def test_works_with_generator_input(self):
        items = (number for number in [1, 2, 3])

        result = list(sliding_window(items, 2))

        self.assertEqual(result, [(1, 2), (2, 3)])

    def test_returns_generator_object(self):
        result = sliding_window([1, 2, 3], 2)

        self.assertIsInstance(result, GeneratorType)

    def test_raises_error_for_invalid_size(self):
        with self.assertRaises(ValueError):
            list(sliding_window([1, 2, 3], 0))


if __name__ == "__main__":
    unittest.main()