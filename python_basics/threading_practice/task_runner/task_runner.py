import threading
import time


def process_task(task_name, results, lock, delay=0.01):
    time.sleep(delay)

    result = f"{task_name} completed"

    with lock:
        results.append(result)


def run_tasks_in_threads(task_names):
    results = []
    threads = []
    lock = threading.Lock()

    for task_name in task_names:
        thread = threading.Thread(
            target=process_task,
            args=(task_name, results, lock),
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results
