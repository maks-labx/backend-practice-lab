def get_open_tickets(tickets):
    for ticket in tickets:
        if ticket["status"] == "open":
            yield ticket