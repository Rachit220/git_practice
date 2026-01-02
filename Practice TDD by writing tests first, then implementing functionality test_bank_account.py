import unittest
from bank_account import BankAccount
class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Rachit", 1000)

    def test_deposit_valid_amount(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw_valid_amount(self):
        self.account.withdraw(400)
        self.assertEqual(self.account.balance, 600)

    def test_withdraw_exact_balance(self):
        self.account.withdraw(1000)
        self.assertEqual(self.account.balance, 0)

    def test_withdraw_more_than_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1500)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-200)
            
    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000)
if __name__ == "__main__":
    unittest.main()
