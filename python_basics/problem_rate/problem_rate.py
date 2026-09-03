def normalize_status(status):
    if not isinstance(status, str):
        raise ValueError("Status must be a string")

    return status.strip().upper()


def calculate_problem_rate(statuses, problem_status="PROBLEM"):
    if not statuses:
        return 0

    normalized_problem_status = normalize_status(problem_status)
    problem_count = 0

    for status in statuses:
        normalized_status = normalize_status(status)

        if normalized_status == normalized_problem_status:
            problem_count += 1

    return round(problem_count / len(statuses) * 100, 2)
