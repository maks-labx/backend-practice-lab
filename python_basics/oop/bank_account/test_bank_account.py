import unittest

from bank_account import BankAccount


class BankAccountTests(unittest.TestCase):
    def test_creates_account_with_owner_and_balance(self):
        account = BankAccount("Max", 100)

        self.assertEqual(account.owner, "Max")
        self.assertEqual(account.balance, 100)

    def test_deposit_increases_balance_and_adds_transaction(self):
        account = BankAccount("Max", 100)

        result = account.deposit(50)

        self.assertEqual(result, 150)
        self.assertEqual(account.balance, 150)
        self.assertIn("Deposit: 50", account.transactions)

    def test_withdraw_decreases_balance_and_adds_transaction(self):
        account = BankAccount("Max", 100)

        result = account.withdraw(40)

        self.assertEqual(result, 60)
        self.assertEqual(account.balance, 60)
        self.assertIn("Withdraw: 40", account.transactions)

    def test_transfer_moves_money_between_accounts(self):
        sender = BankAccount("Max", 100)
        receiver = BankAccount("Anna", 20)

        sender.transfer_to(receiver, 30)

        self.assertEqual(sender.balance, 70)
        self.assertEqual(receiver.balance, 50)

    def test_transfer_adds_transactions_to_both_accounts(self):
        sender = BankAccount("Max", 100)
        receiver = BankAccount("Anna", 20)

        sender.transfer_to(receiver, 30)

        self.assertIn("Transfer to Anna: 30", sender.transactions)
        self.assertIn("Transfer from Max: 30", receiver.transactions)

    def test_get_transaction_history_returns_transactions(self):
        account = BankAccount("Max", 100)

        account.deposit(50)
        account.withdraw(20)

        self.assertEqual(
            account.get_transaction_history(),
            [
                "Initial balance: 100",
                "Deposit: 50",
                "Withdraw: 20",
            ],
        )

    def test_cannot_create_account_with_negative_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("Max", -10)

    def test_cannot_deposit_zero_or_negative_amount(self):
        account = BankAccount("Max", 100)

        with self.assertRaises(ValueError):
            account.deposit(0)

        with self.assertRaises(ValueError):
            account.deposit(-20)

    def test_cannot_withdraw_more_than_balance(self):
        account = BankAccount("Max", 100)

        with self.assertRaises(ValueError):
            account.withdraw(150)

    def test_cannot_transfer_more_than_balance(self):
        sender = BankAccount("Max", 100)
        receiver = BankAccount("Anna", 20)

        with self.assertRaises(ValueError):
            sender.transfer_to(receiver, 150)


if __name__ == "__main__":
    unittest.main()