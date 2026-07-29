from functools import wraps


CALL_LOGS = []


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_entry = {
            "function": func.__name__,
            "args": args,
            "kwargs": kwargs,
        }

        try:
            result = func(*args, **kwargs)
        except Exception as error:
            log_entry["status"] = "error"
            log_entry["error"] = str(error)
            CALL_LOGS.append(log_entry)
            raise

        log_entry["status"] = "success"
        log_entry["result"] = result
        CALL_LOGS.append(log_entry)

        return result

    return wrapper


@log_call
def calculate_total(numbers):
    return sum(numbers)