from concurrent.futures import ProcessPoolExecutor, as_completed


def calculate_square(number):
    return number * number


def calculate_squares_in_processes(numbers, max_workers=None):
    if not numbers:
        return []

    results = [None] * len(numbers)

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        future_to_index = {}

        for index, number in enumerate(numbers):
            future = executor.submit(calculate_square, number)
            future_to_index[future] = index

        for future in as_completed(future_to_index):
            index = future_to_index[future]
            results[index] = future.result()

    return results
