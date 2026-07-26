class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.owner = owner
        self.balance = balance
        self.transactions = []

        if balance > 0:
            self.transactions.append(f"Initial balance: {balance}")

    def deposit(self, amount):
        self._validate_positive_amount(amount, "Deposit amount")

        self.balance += amount
        self.transactions.append(f"Deposit: {amount}")

        return self.balance

    def withdraw(self, amount):
        self._validate_positive_amount(amount, "Withdraw amount")

        if amount > self.balance:
            raise ValueError("Not enough funds")

        self.balance -= amount
        self.transactions.append(f"Withdraw: {amount}")

        return self.balance

    def transfer_to(self, other_account, amount):
        self._validate_positive_amount(amount, "Transfer amount")

        if amount > self.balance:
            raise ValueError("Not enough funds")

        self.balance -= amount
        other_account.balance += amount

        self.transactions.append(f"Transfer to {other_account.owner}: {amount}")
        other_account.transactions.append(f"Transfer from {self.owner}: {amount}")

    def get_transaction_history(self):
        return self.transactions

    def _validate_positive_amount(self, amount, field_name):
        if amount <= 0:
            raise ValueError(f"{field_name} must be greater than 0")