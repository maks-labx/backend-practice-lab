import threading


class SafeCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.value += 1

    def get_value(self):
        with self._lock:
            return self.value


def increment_counter(counter, times):
    for _ in range(times):
        counter.increment()


def run_counter_threads(thread_count, increments_per_thread):
    if thread_count <= 0:
        raise ValueError("thread_count must be greater than 0")

    if increments_per_thread < 0:
        raise ValueError("increments_per_thread cannot be negative")

    counter = SafeCounter()
    threads = []

    for _ in range(thread_count):
        thread = threading.Thread(
            target=increment_counter,
            args=(counter, increments_per_thread),
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return counter.get_value()
