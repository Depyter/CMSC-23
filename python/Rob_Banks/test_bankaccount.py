import unittest
from credit import creditAcc
from debit import debitAcc
from database import Database

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        db = Database()
        account_number_b = db.add_account_to_db("test_user", True, 5000.0, "debit")
        account_number = db.add_account_to_db("test_user", True, 5000.0, "credit")
        self.credit_account = creditAcc("test_user", account_number, True, 5000.0, 10000, 2.5)
        self.debit_account = debitAcc("test_user", account_number_b, True, 5000.0, 2.5)

    def test_credit_deposit(self):
        result = self.credit_account.deposit(2000)
        self.assertTrue(result)
        self.assertEqual(self.credit_account.balance, 3000)

    def test_credit_withdraw(self):
        result = self.credit_account._withdraw(1000)
        self.assertTrue(result)
        self.assertEqual(self.credit_account.balance, 6000)
        res = self.credit_account._withdraw(30000)
        self.assertFalse(res)

    def test_credit_transfer(self):
        result = self.credit_account.transfer(self.debit_account.account_number, 500)
        self.assertTrue(result)
        self.assertEqual(self.credit_account.balance, 5500)
        res = self.credit_account.transfer(self.debit_account.account_number, 20000)
        self.assertFalse(res)

    def test_debit_deposit(self):
        result = self.debit_account.deposit(2000)
        self.assertTrue(result)
        self.assertEqual(self.debit_account.balance, 7000)

    def test_debit_withdraw(self):
        result = self.debit_account._withdraw(1000)
        self.assertTrue(result)
        self.assertEqual(self.debit_account.balance, 4000)
        res = self.debit_account._withdraw(50000)
        self.assertFalse(res)

    def test_debit_transfer(self):
        result = self.debit_account.transfer(self.credit_account.account_number, 400)
        self.assertTrue(result)
        self.assertEqual(self.debit_account.balance, 4600)
        res = self.debit_account.transfer(self.credit_account.account_number, 5000)
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()