class ProblemTicketIterator:
    def __init__(self, tickets, target_status="PROBLEM", min_priority=None):
        self.tickets_iterator = iter(tickets)
        self.target_status = target_status
        self.min_priority = min_priority

    def __iter__(self):
        return self

    def __next__(self):
        for ticket in self.tickets_iterator:
            if ticket.get("status") != self.target_status:
                continue

            if self.min_priority is not None and ticket.get("priority", 0) < self.min_priority:
                continue

            return ticket

        raise StopIteration