def generate_batches(items, batch_size):
    if batch_size <= 0:
        raise ValueError("batch_size must be greater than 0")

    for index in range(0, len(items), batch_size):
        yield items[index:index + batch_size]