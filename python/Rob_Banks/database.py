import sqlite3
import random
import datetime

def generate_unique_account_number():
    con = sqlite3.connect("bank.db")
    cur = con.cursor()
    while True:
        account_number = ''.join([str(random.randint(0,9)) for _ in range(10)])
        res = cur.execute("SELECT account_number FROM registered_bank_accounts WHERE account_number = ?", (account_number,))
        if res.fetchone() is None:
            con.close()
            return int(account_number)

def add_account_to_db(owner: str, status: bool, balance: float, acc_type: str):
    con = sqlite3.connect("bank.db")
    cur = con.cursor()

    # Ensure a table exists otherwise create it
    cur.execute("""
    CREATE TABLE IF NOT EXISTS registered_bank_accounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        owner TEXT, account_number INTEGER, 
        status INTEGER, 
        balance REAL, 
        acc_type TEXT
        )
    """)

    account_number = generate_unique_account_number()
    data = [owner, account_number, 1 if status == True else 0, balance, acc_type]
    cur.execute("INSERT INTO registered_bank_accounts (owner, account_number, status, balance, acc_type) VALUES(?, ?, ?, ?, ?)", data)
    con.commit()
    con.close()
    return account_number

def delete_account_from_db(account_number: int):
    con = sqlite3.connect("bank.db")
    cur = con.cursor()

    # Delete using an account number
    cur.execute("DELETE from registered_bank_accounts WHERE account_number = ?", (account_number,))
    con.commit()
    con.close()

def update_account_bal(account_number, balance):
    con = sqlite3.connect("bank.db")
    cur = con.cursor()

    # Update using an account number
    cur.execute("UPDATE registered_bank_accounts SET balance=? WHERE account_number = ?",(balance, account_number))
    con.commit()
    con.close()

def access_account_db(account_number):
    con = sqlite3.connect("bank.db")
    cur = con.cursor()

    # Access account data 
    res = cur.execute("SELECT balance, acc_type FROM registered_bank_accounts WHERE account_number = ?", (account_number,))
    account = res.fetchone()
    
    con.close()
    if account:
        return account
    else:
        return None

def add_to_transaction_history(account_number, balance, transaction_type, amount):
    con = sqlite3.connect("bank.db")
    cur = con.cursor()
    con.execute("PRAGMA foreign_keys = ON")

    # Ensure the table exists
    cur.execute("""
    CREATE TABLE IF NOT EXISTS transaction_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_number INTEGER,
        balance REAL,
        transaction_type TEXT,
        amount INTEGER,
        new_balance REAL,
        time_of_transaction TIMESTAMP,
        FOREIGN KEY (account_number) REFERENCES registered_bank_accounts(account_number) ON DELETE CASCADE ON UPDATE CASCADE
        )
    """)

    currentDateTime = datetime.datetime.now()
    data = [account_number, balance, transaction_type, amount,balance + amount, currentDateTime]
    cur.execute("""
    INSERT INTO transaction_history (account_number, balance, transaction_type, amount, new_balance, time_of_transaction) 
    VALUES(?, ?, ?, ?, ?, ?)
    """, data)
    con.commit()
    con.close()

def update_db(account_number: int, balance: int, transaction_type: str, amount: int):
    update_account_bal(account_number, balance + amount)
    add_to_transaction_history(account_number, balance, transaction_type, amount)

def balance_report(account_number: int):
    con = sqlite3.connect("bank.db")
    cur = con.cursor()

    # Select all transactions with the account number
    res = cur.execute("SELECT account_number, balance, transaction_type, amount, new_balance, time_of_transaction FROM transaction_history WHERE account_number = ?", (account_number,))
    transactions = res.fetchall()
    con.close()
    if transactions:
        return transactions
    else:
        return None
    