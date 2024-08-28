import os
from customer import Customer
from abc import ABC, abstractmethod
from account import SavingsAccount, CheckingAccount, JointAccount



class BankUserInterface(ABC):
    _customers = []
    __current_customer = None

    @staticmethod
    def create_account():
        print("CREATE AN ACCOUNT")
        print("------------------------------")
        last_name = input("Last Name: ")
        first_name = input("First Name: ")
        birth = input("Birthday: ")
        status = input("Status: ")
        nationality = input("Nationality: ")
        account_type = input("Account Type (Savings/Checking/Joint): ").lower()
        initial_balance = float(input("Initial Deposit:"))

        customer_id = len(BankUserInterface._customers) + 1
        account_number = f"{customer_id:04d}"

        if account_type == "savings":
            if initial_balance < 500:
                print("Savings account requires a minimum initial deposit of 500 PHP.")
                return
        elif account_type == "checking":
            if initial_balance < 25000:
                print("Checking account requires a minimum initial deposit of 25,000 PHP.")
                return
        elif account_type == "joint":
            if initial_balance < 50000:
                print("Joint account requires a minimum initial deposit of 50,000 PHP.")
                return
        else:
            print("------------------------------")
            print("Invalid account type.")
            return

        if account_type == "savings":
            new_account = SavingsAccount(customer_id, account_number, f"{last_name}, {first_name}", account_type, initial_balance)
        elif account_type == "checking":
            new_account = CheckingAccount(customer_id, account_number, f"{last_name}, {first_name}", initial_balance)
        elif account_type == "joint":
            new_account = JointAccount(customer_id, account_number, f"{last_name}, {first_name}", initial_balance)

        existing_customer = next((customer for customer in BankUserInterface._customers if customer.name == f"{last_name}, {first_name}"), None)
        if existing_customer is None:
            existing_customer = Customer(customer_id, f"{last_name}, {first_name}", "", 0)
            BankUserInterface._customers.append(existing_customer)

        existing_customer._accounts.append(new_account)

        BankUserInterface.__current_customer = existing_customer

        print("----------------------------")
        print("Account created successfully. You are now logged in.")
        print("----------------------------")
        input("Press [Enter] to continue.")

    @staticmethod
    def show_menu():
     while True:
        os.system('clear')
        print("------------------------------")
        print("Lykie's Bank")

        if BankUserInterface.__current_customer:
            print("[1] List accounts")
            print("[2] Deposit")
            print("[3] Withdraw")
            print("[4] Check Balance")
            print("[5] Log Out")
            print("[6] Exit")
        else:
            print("[1] Create an account")
            print("[2] Log In")
            print("[7] Exit")

        print("------------------------------")

        choice = input("ENTER CHOICE: ")
        print("------------------------------")

        if choice == '1' and not BankUserInterface.__current_customer:
            BankUserInterface.create_account()
        elif choice == '2' and not BankUserInterface.__current_customer:
            BankUserInterface.log_in()
        elif choice == '7':
            return
        elif not BankUserInterface.__current_customer:
            print("ERROR: Invalid choice. Please create an account, log in, or exit.")
        else:
            if choice == '1':
                BankUserInterface.list_accounts()
            elif choice == '2':
                BankUserInterface.deposit()
            elif choice == '3':
                BankUserInterface.withdraw()
            elif choice == '4':
                BankUserInterface.check_balance()
            elif choice == '5':
                BankUserInterface.log_out()
            elif choice == '6':
                return
            else:
                print("ERROR: Invalid choice. Please try again.")
     
    @staticmethod
    def list_accounts():
     os.system('clear')
     print("------------------------------")
     print("LIST OF ACCOUNTS")
     print("------------------------------")

     customer = BankUserInterface.__current_customer

     if customer is not None:
        print(f"Customer: {customer.name}")
        print("------------------------------")
        print(f"Birthday: {customer.birth}")
        print(f"Status: {customer.status}")
        print(f"Nationality: {customer.nationality}")

        for account in customer._accounts:
            print(f"  Account Number: {account.account_number}")
            print(f"  Account Type: {account.account_type}")
            print(f"  Balance: PHP {account.balance}")
            print("")
     else:
        print("------------------------------")
        print("Please log in to view accounts.")


    @staticmethod
    def deposit():
        os.system('clear')
        print("DEPOSIT TO ACCOUNT")
        print("------------------------------")
        account_number = input("Enter the account number: ")
        amount = float(input("Enter the amount to deposit: "))

        customer = BankUserInterface.__current_customer
        if customer:
            account = next((acc for acc in customer._accounts if acc.account_number == account_number), None)
            if account:
                account.deposit(amount)
                print("Deposit successful.")
            else:
                print("Account not found.")
        else:
            print("Please log in to deposit.")

        input("Press [Enter] to continue.")

    @staticmethod
    def withdraw():
        os.system('clear')
        print("WITHDRAW FROM ACCOUNT")
        print("------------------------------")
        account_number = input("Enter the account number: ")
        amount = float(input("Enter the amount to withdraw: "))

        customer = BankUserInterface.__current_customer
        if customer:
            account = next((acc for acc in customer._accounts if acc.account_number == account_number), None)
            if account:
                account.withdraw(amount)
                print("Withdrawal successful.")
            else:
                print("Account not found.")
        else:
            print("Please log in to withdraw.")

        input("Press [Enter] to continue.")

    @staticmethod
    def check_balance():
        os.system('clear')
        print("CHECK ACCOUNT BALANCE")
        print("------------------------------")
        account_number = input("Enter the account number: ")

        customer = BankUserInterface.__current_customer
        if customer:
            account = next((acc for acc in customer._accounts if acc.account_number == account_number), None)
            if account:
                balance = account.check_balance()
                print(f"Balance in account {account_number}: PHP {balance}")
            else:
                print("Account not found.")
        else:
            print("Please log in to check balance.")

        input("Press [Enter] to continue.")

    @staticmethod
    def log_in():
     print("LOG IN TO AN ACCOUNT")
     print("------------------------------")
     account_number = input("Enter your account number: ")

     found_account = None
     for customer in BankUserInterface._customers:
        for account in customer._accounts:
            if account.account_number == account_number:
                found_account = account
                break
        if found_account:
            break

     if found_account:
        BankUserInterface.__current_customer = customer
        print("Log in successful.")

        # Prompt the user to enter the amount
        #print("------------------------------")
        #amount = float(input("Enter the amount: "))

        while True:
            print("------------------------------")
            print("Lykie's Bank")
            print("[1] List accounts")
            print("[2] Deposit")
            print("[3] Withdraw")
            print("[4] Check Balance")
            print("[5] Log Out")
            print("[6] Exit")
            print("------------------------------")
            choice = input("ENTER CHOICE: ")
            print("------------------------------")

            if choice == '1':
                BankUserInterface.list_accounts()
            elif choice == '2':
                BankUserInterface.deposit()
            elif choice == '3':
                BankUserInterface.withdraw()
            elif choice == '4':
                BankUserInterface.check_balance()
            elif choice == '5':
                BankUserInterface.log_out()
                return
            elif choice == '6':
                return
            else:
                print("ERROR: Invalid choice. Please try again.")
     else:
        num_accounts = sum(len(customer._accounts) for customer in BankUserInterface._customers)
        if num_accounts == 1:
            print("There is no such account. Please create a new account.")
        else:
            print("Account not found. Please try again.")
        print("------------------------------")
        input("Press [Enter] to continue.")

    @staticmethod
    def log_out():
        BankUserInterface.__current_customer = None
        print("Logged out successfully.")
        input("Press [Enter] to continue.")