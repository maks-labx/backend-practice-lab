from functools import wraps


def require_non_empty_list(func):
    @wraps(func)
    def wrapper(items):
        if not items:
            return 0

        return func(items)

    return wrapper


@require_non_empty_list
def calculate_total(items):
    return sum(items)