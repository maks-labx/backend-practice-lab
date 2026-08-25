import queue
import threading
import time


def worker(task_queue, results, lock):
    while True:
        try:
            task_name = task_queue.get_nowait()
        except queue.Empty:
            return

        time.sleep(0.01)
        result = f"{task_name} completed"

        with lock:
            results.append(result)

        task_queue.task_done()


def run_tasks_with_workers(task_names, worker_count=2):
    if worker_count <= 0:
        raise ValueError("worker_count must be greater than 0")

    task_queue = queue.Queue()
    results = []
    threads = []
    lock = threading.Lock()

    for task_name in task_names:
        task_queue.put(task_name)

    for _ in range(worker_count):
        thread = threading.Thread(
            target=worker,
            args=(task_queue, results, lock),
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results
