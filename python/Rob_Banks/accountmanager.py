from database import add_account_to_db, delete_account_from_db
from payroll import payrollAcc
from credit import creditAcc
from debit import debitAcc

from bankaccount import bank_account, transferable
class accountManager():

    def __init__(self, accounts: dict[int, bank_account]):
        # Accounts is a dictionary with keys being accids 
        self.bankaccounts = accounts
        self.currentaccount = None

    # Add a new account 
    def openNewAccount(self, owner: str, acctype: str):
        account_number = add_account_to_db(owner, True, 0.0, acctype)
        print(f"Added new bank account with number: {account_number}")
        if acctype == 'payroll':
            account_object = payrollAcc(owner, account_number, True, 0.0)
        elif acctype == 'credit':
            account_object = creditAcc(owner, account_number, True, 0.0, 25000, 2.6)
        elif acctype == 'debit':
            account_object = debitAcc(owner, account_number, True, 0.0,  2.5,)
        else:
            raise ValueError(f"Unknown account type: {acctype}")
        self.bankaccounts[account_number] = account_object

    def __deleteAccount(self, accid):
        if accid in self.bankaccounts:
            if self.bankaccounts[accid].balance != 0:
                print(f"Cannot delete account with {accid} due to non-zero balance.")
            elif self.bankaccounts[accid].balance == 0:
                delete_account_from_db(accid)
                print("Account successfully deleted.")
            else:
               raise RuntimeError("Unexpected error occurred.")
        else:
            print(f"Enter a valid account number.")
    
    def _accessAccount(self, accid):
        if accid in self.bankaccounts:
            # Set the current account to the bank account object stored  
            self.currentaccount = self.bankaccounts[accid]
            return
        else:
            print(f"Enter a valid account number.")
            return
        
    def _transferFunds(self, toAccount, amount):
        if (isinstance(self.currentaccount, transferable)):
            self.currentaccount.transfer(toAccount, amount)
        else:
            print("Account currently selected cannot transfer funds.")

    # Show all accounts managed by the current instance of account manager
    def _allAccounts(self):
        for account_number, account in self.bankaccounts.items():
            print(f"Account Number: {account_number}")
            print(f"Owner: {account.owner}")
            print(f"Balance: {account.balance}")
            print(f"Account Type: {account.acctype}")
            print("---------------------------")

    def _accountReport(self):
        if self.currentaccount:
            self.currentaccount.balance_report()
        else:
            print("Select one account to check balance report.")

    def _accountoperations(self):
        pass