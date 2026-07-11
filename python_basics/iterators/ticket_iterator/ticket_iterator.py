class TicketIterator:
    def __init__(self, tickets):
        self.tickets = tickets
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.tickets):
            raise StopIteration

        ticket = self.tickets[self.index]
        self.index += 1
        return ticket