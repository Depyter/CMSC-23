from bankaccount import bank_account, transferable  
from database import update_account_bal, access_account_db
class creditAcc(bank_account, transferable):
    
    # use the init of bankaccount but add more info
    def __init__(self, owner:str, account_number: int, status: bool, balance: int, credit_limit: int, interest_rate: float):
        super().__init__(owner, account_number, status, balance)
        self.credit_limit = credit_limit
        self.interest_rate = interest_rate
        self.acctype = 'credit'

    def deposit(self, amount):
        self.balance -= amount
        super().update_to_db(self.account_number, self.balance + amount, 'deposit', - amount)
        return True 

    def _withdraw(self, amount):
        if amount < 0 or amount + self.balance > self.credit_limit:
            return False
        else:
            self.balance += amount
            super().update_to_db(self.account_number, self.balance - amount,'withdraw', amount)
            return True

    def _dueForDeactivation(self):
        return False
    
    def transfer(self, toAccount, amount):
        if self.balance + amount > self.credit_limit:
            return False

        # Get the account from database, returns [balance, acctype]
        account_data = access_account_db(toAccount)
        if not account_data:
            return False  # Handle case where account is not found

        account_balance, account_type = account_data 

        # Reduce balance if account type is credit
        if account_type == 'credit':
            account_balance -= amount
            super().update_to_db(toAccount, account_balance + amount, 'deposit', - amount)
        else:
            account_balance += amount
            super().update_to_db(toAccount, account_balance - amount, 'deposit', amount)

        super().update_to_db(self.account_number, self.balance - amount, 'transfer', amount)
        return True
