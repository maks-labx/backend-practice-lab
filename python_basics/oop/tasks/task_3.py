class Ticket:
    def __init__(self, description, status = "OPEN"):
        self.description = description
        self.status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed_status = ["OPEN", "IN_PROGRESS", "CLOSED"]

        if value not in allowed_status:
            raise ValueError("Incorrect value")
        
        self._status = value

    def close(self):
        self.status = "CLOSED"

    def get_summary(self):
        return f"description: {self.description}, status: {self.status}"

class UrgentTicket(Ticket):
    def __init__(self, description, priority, status = "OPEN"):
        self.priority = priority
        super().__init__(description, status)

    def get_summary(self):
        return super().get_summary() + f", priority: {self.priority}"


ticket1 = Ticket("Broken fridge")
ticket2 = UrgentTicket("Power outage", "HIGH")

print(ticket1.get_summary())

ticket1.status = "IN_PROGRESS"
ticket2.close()

print(ticket1.get_summary())
print(ticket2.get_summary())

ticket1.status = "UNKNOWN"