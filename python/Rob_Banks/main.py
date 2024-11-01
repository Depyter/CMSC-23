from accountmanager import accountManager

# Ideally there would be user authentication and password encryption
# but I think for the purposes of the lab exercise the CRUDE and naive
# way of implementing the user should be fine.
# To get "Bank" level access, input admin.
# Running this file requires python 3.10 as that is version when
# match case was introduced.

def main():
    username = input("Enter the username to access the account manager: ")
    manager = accountManager(username)
    manager._accountManagerOperations()

if __name__ == "__main__":
    main() 