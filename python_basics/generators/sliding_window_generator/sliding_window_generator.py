from collections import deque


def sliding_window(items, size):
    if size <= 0:
        raise ValueError("size must be greater than 0")

    window = deque(maxlen=size)

    for item in items:
        window.append(item)

        if len(window) == size:
            yield tuple(window)