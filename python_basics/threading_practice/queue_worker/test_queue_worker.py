import unittest

from queue_worker import run_tasks_with_workers


class QueueWorkerTests(unittest.TestCase):
    def test_runs_all_tasks_with_workers(self):
        task_names = ["task-1", "task-2", "task-3", "task-4"]

        result = run_tasks_with_workers(task_names, worker_count=2)

        self.assertEqual(
            sorted(result),
            sorted(
                [
                    "task-1 completed",
                    "task-2 completed",
                    "task-3 completed",
                    "task-4 completed",
                ]
            ),
        )

    def test_empty_task_list_returns_empty_result(self):
        result = run_tasks_with_workers([], worker_count=2)

        self.assertEqual(result, [])

    def test_worker_count_can_be_greater_than_task_count(self):
        task_names = ["task-1", "task-2"]

        result = run_tasks_with_workers(task_names, worker_count=5)

        self.assertEqual(
            sorted(result),
            sorted(
                [
                    "task-1 completed",
                    "task-2 completed",
                ]
            ),
        )

    def test_result_count_matches_task_count(self):
        task_names = ["task-1", "task-2", "task-3"]

        result = run_tasks_with_workers(task_names, worker_count=2)

        self.assertEqual(len(result), 3)

    def test_invalid_worker_count_raises_error(self):
        with self.assertRaises(ValueError):
            run_tasks_with_workers(["task-1"], worker_count=0)


if __name__ == "__main__":
    unittest.main()
