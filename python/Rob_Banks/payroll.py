from bankaccount import bank_account
class payrollAcc(bank_account):

    # use the init of bankaccount but add more info
    def __init__(self, owner:str, account_number: int, status: bool, balance: int):
        super().__init__(owner, account_number, status, balance)
        self.acctype = 'payroll'

    def deposit(self, amount: int):
        self.balance += amount
        super().update_to_db(self.account_number, self.balance - amount,'deposit', amount)
        return True 

    def _withdraw(self, amount):
        if amount < 0 or amount > self.balance:
            return False
        else:
            self.balance -= amount
            super().update_to_db(self.account_number, self.balance + amount, 'withdraw', - amount)
            return True

    def _dueForDeactivation(self):
        return False