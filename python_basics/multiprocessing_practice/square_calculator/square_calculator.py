import multiprocessing


def calculate_square(number):
    return number * number


def calculate_squares_in_processes(numbers):
    if not numbers:
        return []

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_square, numbers)

    return results
