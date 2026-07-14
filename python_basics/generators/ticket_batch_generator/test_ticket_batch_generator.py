import unittest
from types import GeneratorType

from ticket_batch_generator import generate_batches


class TicketBatchGeneratorTests(unittest.TestCase):
    def test_generates_batches_with_equal_size(self):
        items = ["t1", "t2", "t3", "t4"]

        result = list(generate_batches(items, 2))

        self.assertEqual(result, [["t1", "t2"], ["t3", "t4"]])

    def test_last_batch_can_be_smaller(self):
        items = ["t1", "t2", "t3", "t4", "t5"]

        result = list(generate_batches(items, 2))

        self.assertEqual(result, [["t1", "t2"], ["t3", "t4"], ["t5"]])

    def test_returns_generator_object(self):
        items = ["t1", "t2"]

        result = generate_batches(items, 2)

        self.assertIsInstance(result, GeneratorType)

    def test_raises_error_for_invalid_batch_size(self):
        with self.assertRaises(ValueError):
            list(generate_batches(["t1", "t2"], 0))


if __name__ == "__main__":
    unittest.main()