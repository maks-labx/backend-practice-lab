class ProblemTicketIterator:
    def __init__(self, tickets, target_status="PROBLEM"):
        self.tickets = tickets
        self.target_status = target_status
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.tickets):
            ticket = self.tickets[self.index]
            self.index += 1

            if ticket.get("status") == self.target_status:
                return ticket

        raise StopIteration