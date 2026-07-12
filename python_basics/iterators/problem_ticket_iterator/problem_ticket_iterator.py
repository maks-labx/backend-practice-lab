class ProblemTicketIterator:
    def __init__(self, tickets):
        self.tickets = tickets
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.tickets):
            ticket = self.tickets[self.index]
            self.index += 1

            if ticket["status"] == "PROBLEM":
                return ticket

        raise StopIteration