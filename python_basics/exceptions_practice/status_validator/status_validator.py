class InvalidStatusError(ValueError):
    pass


def validate_status(status, allowed_statuses=None):
    if allowed_statuses is None:
        allowed_statuses = {"new", "in_progress", "done"}

    normalized_status = status.strip().lower()

    if normalized_status not in allowed_statuses:
        raise InvalidStatusError(f"Invalid status: {status}")

    return normalized_status
