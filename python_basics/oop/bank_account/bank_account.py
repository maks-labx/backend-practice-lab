class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than 0")

        if amount > self.balance:
            raise ValueError("Not enough funds")

        self.balance -= amount
        return self.balance