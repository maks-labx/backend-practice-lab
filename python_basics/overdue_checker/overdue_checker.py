from datetime import date


def is_overdue(due_date, today=None):
    _validate_date(due_date, "due_date")
    today = _get_today(today)

    return due_date < today


def get_due_status(due_date, today=None):
    _validate_date(due_date, "due_date")
    today = _get_today(today)

    if due_date < today:
        return "overdue"

    if due_date == today:
        return "due_today"

    return "upcoming"


def days_until_due(due_date, today=None):
    _validate_date(due_date, "due_date")
    today = _get_today(today)

    return (due_date - today).days


def _get_today(today):
    if today is None:
        return date.today()

    _validate_date(today, "today")
    return today


def _validate_date(value, field_name):
    if not isinstance(value, date):
        raise ValueError(f"{field_name} must be a date")