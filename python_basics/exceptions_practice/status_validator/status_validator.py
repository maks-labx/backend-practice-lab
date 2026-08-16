class InvalidStatusError(ValueError):
    pass


DEFAULT_ALLOWED_STATUSES = {"new", "in_progress", "done"}


def validate_status(status, allowed_statuses=None):
    if allowed_statuses is None:
        allowed_statuses = DEFAULT_ALLOWED_STATUSES

    if not isinstance(status, str):
        raise InvalidStatusError("Status must be a string")

    normalized_status = status.strip().lower()

    if not normalized_status:
        raise InvalidStatusError("Status cannot be empty")

    if normalized_status not in allowed_statuses:
        raise InvalidStatusError(f"Invalid status: {status}")

    return normalized_status


def validate_statuses(statuses, allowed_statuses=None):
    return [validate_status(status, allowed_statuses) for status in statuses]
