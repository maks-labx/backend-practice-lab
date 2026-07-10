import unittest

from log_call import CALL_LOGS, calculate_total


class LogCallTests(unittest.TestCase):
    def setUp(self):
        CALL_LOGS.clear()

    def test_returns_original_function_result(self):
        result = calculate_total([10, 20, 30])

        self.assertEqual(result, 60)

    def test_adds_log_message_when_function_is_called(self):
        calculate_total([1, 2, 3])

        self.assertEqual(CALL_LOGS, ["Called function: calculate_total"])


if __name__ == "__main__":
    unittest.main()