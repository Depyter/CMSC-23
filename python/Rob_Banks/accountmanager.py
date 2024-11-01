from abc import ABC, abstractmethod
from database import Database
from payroll import payrollAcc
from credit import creditAcc
from debit import debitAcc
from bankaccount import bank_account, transferable

class account_change(ABC):
    @abstractmethod
    def monthlyChanges(self) -> None:
        pass

class accountManager(account_change):

    def __init__(self, username: str):
        self.username = username
        db = Database()
        # Load accounts from database whose owner is the user
        accounts = db.load_accounts_from_db(username) 
        if accounts is not None:
            self.bankaccounts = {}
            # Individually create the objects 
            for account in accounts:
                # Unpack the account tuple which is [acc_num, status, balance, acctype]
                owner, account_number, status, balance, acctype = account
                self.bankaccounts[account_number] = self.__create_account_object(owner, account_number, status, balance, acctype)
        else: 
            self.bankaccounts = {}
        self.currentaccount = None

    def monthlyChanges(self):
        for account_number, account in self.bankaccounts:
            if account.acctype == 'credit' or account.acctype == 'debit':
                account.balance += self.interest_rate * 0.01 * account.balance

            if account._dueForDeactivation():
                account.status = False

    def __create_account_object(self, owner, account_number, status, balance, acctype):
        if acctype == 'payroll':
            return payrollAcc(owner, account_number, status, balance)
        elif acctype == 'credit':
            return creditAcc(owner, account_number, status, balance, 25000, 2.6)
        elif acctype == 'debit':
            return debitAcc(owner, account_number, status, balance,  2.5,)
        else:
            raise ValueError(f"Unknown account type: {acctype}") 
    
    # Add a new account 
    def __openNewAccount(self, owner: str, acctype: str):
        db = Database()
        account_number = db.add_account_to_db(owner, True, 0.0, acctype)
        print(f"Added new bank account with number: {account_number}")
        account_object = self.__create_account_object(owner, account_number, True, 0.0, acctype)
        self.bankaccounts[account_number] = account_object

    def __deleteAccount(self, accid):
        if accid in self.bankaccounts:
            if self.bankaccounts[accid].balance != 0:
                print(f"Cannot delete account with {accid} due to non-zero balance.")

            elif self.bankaccounts[accid].balance == 0:
                db = Database()
                db.delete_account_from_db(accid)

                if self.currentaccount and self.currentaccount.account_number == accid:
                    self.currentaccount = None
                del self.bankaccounts[accid]
                print(f"Account with number {accid} successfully deleted.")
            else:
               raise RuntimeError("Unexpected error occurred.")
        else:
            print(f"Enter a valid account number.")
    
    def __accessAccount(self, accid):
        if accid in self.bankaccounts:
            # Set the current account to the bank account object stored  
            self.currentaccount = self.bankaccounts[accid]
            self.__currentAccountOperations()
            return
        else:
            print(f"Enter a valid account number.")
            return
        
    def __transferFunds(self, toAccount, amount):
        if self.currentaccount.transfer(toAccount, amount):
            print(f"Transferred {amount} succfessfully to {toAccount}")
        else:
            print("Transfer failed. Please try again.")

    def __showAccountinformation(self, account_number: int, account: bank_account):
        print("---------------------------")
        print(f"Account Number: {account_number}")
        print(f"Owner: {account.owner}")
        print(f"Balance: {account.balance}")
        print(f"Account Type: {account.acctype}")
        print("---------------------------")

    # Show all accounts managed by the current instance of account manager
    def __showAllAccounts(self):
        for account_number, account in self.bankaccounts.items():
            self.__showAccountinformation(account_number, account)
    
    def __showCurrentAccount(self):
        if self.currentaccount is not None:
            self.__showAccountinformation(self.currentaccount.account_number, self.currentaccount)

    def __accountReport(self):
        if self.currentaccount:
            self.currentaccount.balance_report()
        else:
            print("Select one account to check balance report.")

    def __monthlyCheck(self):
        pass

    def __currentAccountOperations(self):
        while True:
            print("Account operations:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer funds (For non-payroll accounts)")
            print("4. Balance report")
            print("5. Exit this menu")
            choice = input("Enter your choice: ")
        
            match choice:
                case '1':
                    amount = self.__get_valid_amount("Enter amount to deposit: ")
                    self.currentaccount.deposit(amount)
                case '2':
                    amount = self.__get_valid_amount("Enter amount to withdraw: ")
                    self.currentaccount._withdraw(amount)
                case '3':
                    if isinstance(self.currentaccount, transferable):
                        toAccount = self.__get_valid_account_number("Enter account number to transfer funds to: ")
                        amount = self.__get_valid_amount("Enter amount to transfer: ")
                        self.__transferFunds(toAccount, amount)
                    else:
                        print("Cannot transfer with current account.")
                case '4':
                    self.__accountReport()
                case '5':
                    print("Exiting program.")
                    break
                case _:
                    print("Invalid choice. Please try again.")

    def _accountManagerOperations(self):
        while True:
            print("Account manager operations:")
            print("1. Select account to access")
            print("2. Show all accounts")
            print("3. Show current account")
            print("4. Open a new account")
            print("5. Delete account")
            print("6. Exit")
            choice = input("Enter your choice: ")

            match choice:
                case '1':
                    accid = self.__get_valid_account_number("Enter the account number you want to access: ")
                    self.__accessAccount(accid)
                case '2':
                    self.__showAllAccounts()
                case '3':
                    self.__showCurrentAccount()
                case '4':
                    owner = self.username
                    print("1: Payroll")
                    print("2: Debit")
                    print("3: Credit")
                    acctype = self.__get_valid_account_type("Enter the number of your chosen account type: ")
                    self.__openNewAccount(owner, acctype)
                case '5':
                    accid = self.__get_valid_account_number("Enter the account number to delete: ")
                    self.__deleteAccount(accid)
                case '6':
                    print("Exiting program.")
                    break
                case _:
                    print("Invalid choice. Please try again.")

    def __get_valid_account_type(self, prompt):
        acctypes = {1: 'payroll', 2: 'debit', 3 : 'credit'}
        while True:
            try: 
                acctype = int(input(prompt))
                if acctypes[acctype]:
                    return acctypes[acctype]
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number")

    def __get_valid_account_number(self, prompt):
        while True:
            try:
                account_number = int(input(prompt))
                if account_number > 0:
                    return account_number
                else:
                    print("Account number is not valid. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid account number.")

    def __get_valid_amount(self, prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount > 0:
                    return amount
                else:
                    print("Amount must be positive. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")