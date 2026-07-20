def get_tickets_by_status(tickets, status="open", min_priority=None):
    for ticket in tickets:
        if ticket.get("status") != status:
            continue

        if min_priority is not None and ticket.get("priority", 0) < min_priority:
            continue

        yield ticket
