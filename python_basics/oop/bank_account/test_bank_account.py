import unittest

from bank_account import BankAccount


class BankAccountTests(unittest.TestCase):
    def test_creates_account_with_owner_and_balance(self):
        account = BankAccount("Max", 100)

        self.assertEqual(account.owner, "Max")
        self.assertEqual(account.balance, 100)

    def test_deposit_increases_balance(self):
        account = BankAccount("Max", 100)

        result = account.deposit(50)

        self.assertEqual(result, 150)
        self.assertEqual(account.balance, 150)

    def test_withdraw_decreases_balance(self):
        account = BankAccount("Max", 100)

        result = account.withdraw(40)

        self.assertEqual(result, 60)
        self.assertEqual(account.balance, 60)

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


if __name__ == "__main__":
    unittest.main()