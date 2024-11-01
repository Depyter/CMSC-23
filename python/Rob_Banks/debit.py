from bankaccount import bank_account, transferable
from database import Database
class debitAcc(bank_account, transferable):
    
    # use the init of bankaccount but add more info
    def __init__(self, owner:str, account_number: int, status: bool, balance: float, interest_rate: float):
        super().__init__(owner, account_number, status, balance)
        self.minimum_balance = 3000
        self.interest_rate = interest_rate
        self.acctype = 'debit'

    def deposit(self, amount: int):
        self.balance += amount
        original_bal = self.balance - amount
        super().update_to_db(self.account_number, original_bal, 'deposit', amount)
        return True 

    def _withdraw(self, amount):
        if amount < 0 or amount > self.balance:
            return False
        else:
            self.balance -= amount
            super().update_to_db(self.account_number, self.balance + amount, 'withdraw', - amount)
            return True

    def _dueForDeactivation(self):
        return self.balance < self.minimum_balance
    
    def transfer(self, toAccount, amount):
        if amount > self.balance:
            return False

        # Get the account from database, returns [balance, acctype]
        db = Database()
        account_data = db.access_account_db(toAccount)
        if not account_data:
            return False  # Handle case where account is not found

        account_balance, account_type = account_data 
        self.balance -= amount
        
        # Reduce balance if account type is credit
        if account_type == 'credit':
            account_balance -= amount
            super().update_to_db(toAccount, account_balance + amount, 'deposit', - amount)
        else:
            account_balance += amount
            super().update_to_db(toAccount, account_balance - amount, 'deposit', amount)

        super().update_to_db(self.account_number, self.balance + amount, 'transfer', - amount)
        return True