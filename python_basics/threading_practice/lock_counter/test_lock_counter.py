import unittest

from lock_counter import SafeCounter, run_counter_threads


class LockCounterTests(unittest.TestCase):
    def test_safe_counter_increment_increases_value(self):
        counter = SafeCounter()

        counter.increment()
        counter.increment()

        self.assertEqual(counter.get_value(), 2)

    def test_run_counter_threads_returns_expected_count(self):
        result = run_counter_threads(
            thread_count=5,
            increments_per_thread=100,
        )

        self.assertEqual(result, 500)

    def test_run_counter_threads_with_one_thread(self):
        result = run_counter_threads(
            thread_count=1,
            increments_per_thread=10,
        )

        self.assertEqual(result, 10)

    def test_run_counter_threads_with_zero_increments(self):
        result = run_counter_threads(
            thread_count=3,
            increments_per_thread=0,
        )

        self.assertEqual(result, 0)

    def test_invalid_thread_count_raises_error(self):
        with self.assertRaises(ValueError):
            run_counter_threads(
                thread_count=0,
                increments_per_thread=10,
            )

    def test_invalid_increment_count_raises_error(self):
        with self.assertRaises(ValueError):
            run_counter_threads(
                thread_count=3,
                increments_per_thread=-1,
            )


if __name__ == "__main__":
    unittest.main()
