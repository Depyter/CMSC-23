from abc import ABC, abstractmethod
from database import Database
# Define an abstract class to access these accounts
class bank_account(ABC):

    def __init__(self, owner:str, account_number:int, status:bool, start_bal:float):
        self.owner = owner
        self.account_number = account_number
        self.status = status
        self.balance = start_bal
        self.acctype = None

    @classmethod
    # Call the update db function to update the transaction history table and bank account table
    def update_to_db(self, account_number: int, balance: int, transaction_type: str, amount: int):
        db = Database()
        db.update_db(account_number, balance, transaction_type, amount)
    
    def balance_report(self):
        db = Database()
        transactions = db.balance_report(self.account_number)
        if transactions is not None:
            for transaction in transactions:
                account_number, balance, transaction_type, amount, new_balance, time_of_transaction = transaction
                print(f"Account Number: {account_number}")
                print(f"Balance: {balance}")
                print(f"Transaction Type: {transaction_type}")
                print(f"Amount: {amount}")
                print(f"New Balance: {new_balance}")
                print(f"Time of Transaction: {time_of_transaction}")
                print("---------------------------")
        else:
            print("Nothing to show for balance report.")
        
    @abstractmethod
    # Deposit money, let subclass override
    def deposit(self, amount):
        pass

    @abstractmethod
    # Withdraw money, let subclass override
    def _withdraw(self, amount):
        pass

    # Return balance
    def getbalance(self):
        return self.balance
    
    # Return current account status
    def _getStatus(self):
        return self.status

    # Return account number
    def _getAccountnumber(self):
        return self.acc_number
    
    # Return account name
    def _getAccountname(self):
        return self.owner
    
    @abstractmethod
    # Let the subclasses override how if they are for deactivation
    def _dueForDeactivation(self) -> bool:
        pass

class transferable(ABC):
    @abstractmethod
    def transfer(self, toAccount, amount) -> bool:
        pass

