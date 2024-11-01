import unittest
import sqlite3
from database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Set up the shared in-memory database URI
        self.db_uri = 'file:memdb1?mode=memory&cache=shared'

        # Connect to the shared in-memory database
        self.connection = sqlite3.connect(self.db_uri, uri=True)
        self.cursor = self.connection.cursor()

        # Create the necessary tables
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS registered_bank_accounts (
            account_number INTEGER PRIMARY KEY,
            owner TEXT,
            status BOOLEAN,
            balance REAL,
            acc_type TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaction_history (
            account_number INTEGER,
            balance REAL,
            transaction_type TEXT,
            amount REAL,
            new_balance REAL,
            time_of_transaction TIMESTAMP,
            FOREIGN KEY (account_number) REFERENCES registered_bank_accounts(account_number) ON DELETE CASCADE ON UPDATE CASCADE
        )
        """)

        # Insert initial data
        self.cursor.executemany(
            "INSERT INTO registered_bank_accounts (account_number, owner, status, balance, acc_type) VALUES (?, ?, ?, ?, ?)",
            [
                (14174005, 'test_user', 1, 1000.0, 'debit'),
                (7325506398, 'test_user', 1, 1000.0, 'debit'),
                (3283845673, 'test_user', 1, 1000.0, 'debit')
            ]
        )
        self.connection.commit()

        # Create an instance of Database pointing to the same shared in-memory database
        self.db = Database(db_name=self.db_uri)

    def tearDown(self):
        # Close the database connection
        self.connection.close()

    def test_add_account_to_db(self):
        owner = "test_user"
        status = True
        balance = 1000.0
        acctype = "debit"
        account_number = self.db.add_account_to_db(owner, status, balance, acctype)
        self.assertIsNotNone(account_number)

    def test_access_account_db(self):
        account_number = 14174005
        account_data = self.db.access_account_db(account_number)
        self.assertIsNotNone(account_data)
        self.assertEqual(len(account_data), 2)

    def test_update_account_bal(self):
        account_number = 7325506398
        new_balance = 2000.0
        self.db.update_account_bal(account_number, new_balance)
        account_data = self.db.access_account_db(account_number)
        balance, acctype = account_data
        self.assertEqual(balance, new_balance)

    def test_delete_account_from_db(self):
        account_number = 3283845673
        self.db.delete_account_from_db(account_number)
        account_data = self.db.access_account_db(account_number)
        self.assertIsNone(account_data)

    def test_add_to_transaction_history(self):
        account_number = 14174005  # Existing account number
        balance = 1000.0
        transaction_type = "deposit"
        amount = 500.0

        # Add transaction to history
        self.db.add_to_transaction_history(account_number, balance, transaction_type, amount)

        # Query the transaction_history table to check if the transaction was added
        self.cursor.execute("""
        SELECT account_number, balance, transaction_type, amount, new_balance, time_of_transaction
        FROM transaction_history
        WHERE account_number = ?
        """, (account_number,))
        transactions = self.cursor.fetchall()

        self.assertEqual(len(transactions), 1)
        transaction = transactions[0]
        self.assertEqual(transaction[0], account_number)
        self.assertEqual(transaction[1], balance)
        self.assertEqual(transaction[2], transaction_type)
        self.assertEqual(transaction[3], amount)
        self.assertEqual(transaction[4], balance + amount)

if __name__ == '__main__':
    unittest.main()