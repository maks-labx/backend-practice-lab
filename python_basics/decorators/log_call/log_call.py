from functools import wraps


CALL_LOGS = []


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        CALL_LOGS.append(f"Called function: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log_call
def calculate_total(numbers):
    return sum(numbers)