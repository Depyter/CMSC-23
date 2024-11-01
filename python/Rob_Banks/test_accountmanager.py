import unittest
from accountmanager import accountManager

class TestAccountManager(unittest.TestCase):

    def setUp(self):
        self.username = "account_test"
        self.manager = accountManager(self.username)

    def test_account_manager_initialization(self):
        self.assertEqual(self.manager.username, self.username)
        self.assertIsNotNone(self.manager.bankaccounts)
        self.assertIsNone(self.manager.currentaccount)

    def test_open_new_account(self):
        initial_account_count = len(self.manager.bankaccounts)
        self.manager._accountManager__openNewAccount(self.username, "debit")
        self.assertEqual(len(self.manager.bankaccounts), initial_account_count + 1)

    def test_delete_account(self):
        self.manager._accountManager__openNewAccount(self.username, "debit")
        account_number = list(self.manager.bankaccounts.keys())[0]
        self.manager._accountManager__deleteAccount(account_number)
        self.assertNotIn(account_number, self.manager.bankaccounts)

if __name__ == '__main__':
    unittest.main()