def count_statuses(statuses):
    result = {}

    for status in statuses:
        if status in result:
            result[status] += 1
        else:
            result[status] = 1

    return result

if __name__ == "__main__":
    sample_statuses = ["OK", "PROBLEM", "OK", "PROBLEM", "OK"]
    print(count_statuses(sample_statuses))