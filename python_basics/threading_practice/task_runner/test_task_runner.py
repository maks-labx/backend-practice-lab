import unittest

from task_runner import run_tasks_in_threads


class TaskRunnerTests(unittest.TestCase):
    def test_runs_all_tasks(self):
        task_names = ["task-1", "task-2", "task-3"]

        result = run_tasks_in_threads(task_names)

        self.assertEqual(
            sorted(result, key=lambda item: item["task"]),
            [
                {"task": "task-1", "status": "completed"},
                {"task": "task-2", "status": "completed"},
                {"task": "task-3", "status": "completed"},
            ],
        )

    def test_empty_task_list_returns_empty_result(self):
        result = run_tasks_in_threads([])

        self.assertEqual(result, [])

    def test_result_count_matches_task_count(self):
        task_names = ["task-1", "task-2", "task-3", "task-4"]

        result = run_tasks_in_threads(task_names)

        self.assertEqual(len(result), 4)

    def test_failed_task_returns_failed_status(self):
        task_names = ["task-1", "task-2", "task-3"]

        result = run_tasks_in_threads(
            task_names,
            failed_task_names={"task-2"},
        )

        sorted_result = sorted(result, key=lambda item: item["task"])

        self.assertEqual(
            sorted_result,
            [
                {"task": "task-1", "status": "completed"},
                {
                    "task": "task-2",
                    "status": "failed",
                    "error": "task-2 failed",
                },
                {"task": "task-3", "status": "completed"},
            ],
        )

    def test_other_tasks_continue_if_one_task_fails(self):
        task_names = ["task-1", "task-2", "task-3"]

        result = run_tasks_in_threads(
            task_names,
            failed_task_names={"task-2"},
        )

        completed_tasks = [
            item["task"] for item in result if item["status"] == "completed"
        ]

        self.assertEqual(
            sorted(completed_tasks),
            ["task-1", "task-3"],
        )


if __name__ == "__main__":
    unittest.main()
