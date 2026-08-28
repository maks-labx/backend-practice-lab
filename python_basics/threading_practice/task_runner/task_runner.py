import threading
import time


def process_task(task_name, results, lock, failed_task_names=None, delay=0.01):
    try:
        time.sleep(delay)

        if failed_task_names and task_name in failed_task_names:
            raise ValueError(f"{task_name} failed")

        result = {
            "task": task_name,
            "status": "completed",
        }
    except Exception as error:
        result = {
            "task": task_name,
            "status": "failed",
            "error": str(error),
        }

    with lock:
        results.append(result)


def run_tasks_in_threads(task_names, failed_task_names=None):
    results = []
    threads = []
    lock = threading.Lock()

    if failed_task_names is None:
        failed_task_names = set()

    for task_name in task_names:
        thread = threading.Thread(
            target=process_task,
            args=(task_name, results, lock, failed_task_names),
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results
