import unittest

from task_runner import run_tasks_in_threads


class TaskRunnerTests(unittest.TestCase):
    def test_runs_all_tasks(self):
        task_names = ["task-1", "task-2", "task-3"]

        result = run_tasks_in_threads(task_names)

        self.assertEqual(
            sorted(result),
            sorted(
                [
                    "task-1 completed",
                    "task-2 completed",
                    "task-3 completed",
                ]
            ),
        )

    def test_empty_task_list_returns_empty_result(self):
        result = run_tasks_in_threads([])

        self.assertEqual(result, [])

    def test_result_count_matches_task_count(self):
        task_names = ["task-1", "task-2", "task-3", "task-4"]

        result = run_tasks_in_threads(task_names)

        self.assertEqual(len(result), 4)


if __name__ == "__main__":
    unittest.main()
