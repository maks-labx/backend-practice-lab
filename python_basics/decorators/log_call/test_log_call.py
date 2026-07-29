import unittest

from log_call import CALL_LOGS, calculate_total, log_call


class LogCallTests(unittest.TestCase):
    def setUp(self):
        CALL_LOGS.clear()

    def test_returns_original_function_result(self):
        result = calculate_total([10, 20, 30])

        self.assertEqual(result, 60)

    def test_adds_success_log_entry(self):
        calculate_total([10, 20, 30])

        self.assertEqual(len(CALL_LOGS), 1)
        self.assertEqual(CALL_LOGS[0]["function"], "calculate_total")
        self.assertEqual(CALL_LOGS[0]["args"], ([10, 20, 30],))
        self.assertEqual(CALL_LOGS[0]["kwargs"], {})
        self.assertEqual(CALL_LOGS[0]["status"], "success")
        self.assertEqual(CALL_LOGS[0]["result"], 60)

    def test_logs_kwargs(self):
        @log_call
        def greet_user(name, greeting="Hello"):
            return f"{greeting}, {name}"

        result = greet_user("Max", greeting="Hi")

        self.assertEqual(result, "Hi, Max")
        self.assertEqual(CALL_LOGS[0]["function"], "greet_user")
        self.assertEqual(CALL_LOGS[0]["args"], ("Max",))
        self.assertEqual(CALL_LOGS[0]["kwargs"], {"greeting": "Hi"})
        self.assertEqual(CALL_LOGS[0]["status"], "success")
        self.assertEqual(CALL_LOGS[0]["result"], "Hi, Max")

    def test_logs_error_and_raises_exception(self):
        @log_call
        def fail_task():
            raise ValueError("Something went wrong")

        with self.assertRaises(ValueError):
            fail_task()

        self.assertEqual(len(CALL_LOGS), 1)
        self.assertEqual(CALL_LOGS[0]["function"], "fail_task")
        self.assertEqual(CALL_LOGS[0]["status"], "error")
        self.assertEqual(CALL_LOGS[0]["error"], "Something went wrong")

    def test_preserves_original_function_name(self):
        self.assertEqual(calculate_total.__name__, "calculate_total")


if __name__ == "__main__":
    unittest.main()
