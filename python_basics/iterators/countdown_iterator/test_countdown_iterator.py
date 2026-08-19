import unittest

from countdown_iterator import CountdownIterator


class CountdownIteratorTests(unittest.TestCase):
    def test_iterates_from_start_to_one(self):
        result = list(CountdownIterator(5))

        self.assertEqual(result, [5, 4, 3, 2, 1])

    def test_start_zero_returns_empty_list(self):
        result = list(CountdownIterator(0))

        self.assertEqual(result, [])

    def test_next_returns_numbers_one_by_one(self):
        iterator = CountdownIterator(3)

        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 1)

        with self.assertRaises(StopIteration):
            next(iterator)

    def test_negative_start_raises_error(self):
        with self.assertRaises(ValueError):
            CountdownIterator(-1)


if __name__ == "__main__":
    unittest.main()
