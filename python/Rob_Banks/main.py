from accountmanager import accountManager

def main():
    username = input("Enter the username to access the account manager: ")
    manager = accountManager(username)
    manager._accountManagerOperations()

if __name__ == "__main__":
    main() 