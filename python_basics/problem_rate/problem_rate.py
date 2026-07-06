def calculate_problem_rate(statuses):
    if not statuses:
        return 0

    problem_count = 0

    for status in statuses:
        if status == "PROBLEM":
            problem_count += 1

    return problem_count / len(statuses) * 100