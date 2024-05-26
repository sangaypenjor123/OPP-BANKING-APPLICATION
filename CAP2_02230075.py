################################
# Name: sangay penjor
# Deparment: Electrical Deparment
# STudent ID no: 02230075
################################
# REFERENCES
#Sutor, R. S. (2021). Dancing with Python: Learn to Code with Python and Quantum Computing. United Kingdom: Packt Publishing.
################################

import random

class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number  # Assign the account number.
        self.balance = balance  # Adjust the account balance accordingly.
        self.account_type = account_type  # Decide on the account type.

    def deposit(self, amount):
        self.balance += amount  #The money deposited gets added to the total.
        return self.balance  # Considering the improved balance

    def withdraw(self, amount):
        if amount <= self.balance:  # Check to see if the withdrawal amount matches or falls short of the remaining balance.
            self.balance -= amount  # Take the money out of your account.
            return self.balance  # Given the new balance.
        else:
            return "Insufficient funds"  # Should the withdrawal amount exceed the balance, a return message will be sent.

class PersonalAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Personal")  # Guidelines for the kind of personal account

class BusinessAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Business")  # making for the sort of business account.
class Bank:
    def __init__(self):
        self.accounts = {}  # To store accounts, an empty dictionary is established.

    def create_account(self, account_type):
        account_number = random.randint(10000, 99999)  #An arbitrary account number is produced.
        balance = 0  # Put the balance to zero.
        if account_type.lower() == "personal":
            account = PersonalAccount(account_number, balance)  # Create a thing for your own account.
        elif account_type.lower() == "business":
            account = BusinessAccount(account_number, balance)  # Create a piece of content for your company account.
        else:
            return "Invalid account type"  # Returned message for an unsupported account type
        
        with open("accounts.txt", "a") as file:
            file.write(f"{account_number},{account_type},{balance}\n")  # Add account details to the document.
        
        self.accounts[account_number] = account  # Add account details to the dictionary
        return account_number  # Account number that appears back

    def login(self, account_number):
        with open("accounts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if int(data[0]) == account_number:
                    account_type = data[1]
                    balance = float(data[2])
                    if account_type == "Personal":
                        return PersonalAccount(account_number, balance)  #Reconnect the personal account object back in.
                    elif account_type == "Business":
                        return BusinessAccount(account_number, balance)  #return the business account item.
                    else:
                        return None  # Return None if the account type is unknown.


    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)  # sum that was added to the account
        else:
            return "Account not found"  # A message is returned in case there is no account.

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)  # Remove funds from the account.
            
        else:
            return "Account not found"  # If there isn't an account, a reply is sent..
    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]  # Take the account out of a dictionary.
            with open("accounts.txt", "r") as file:
                lines = file.readlines()  # Go through the file line by line.
            with open("accounts.txt", "w") as file:
                for line in lines:
                    if line.split(",")[0] != str(account_number):
                        file.write(line)  # without deleting the deleted account, rebuild the file.
            return "Account deleted"  # Message returned following successful deletion
        else:
            return "Account not found"  # If there is no account, a message is returned.


def main():
    bank = Bank()  # Construct a bank object.
    while True:
        print("\n1. Open Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            account_type = input("Enter account type (Personal/Business): ")
            account_number = bank.create_account(account_type)  # Create a new account.
            print(f"Account created successfully with number: {account_number}")
        elif choice == "2":
            account_number = int(input("Enter account number: "))
            account = bank.login(account_number)  # Log in to access your present account.
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Delete Account")
                    print("4. Logout")
                    operation = input("Enter operation choice: ")
                    if operation == "1":
                        amount = float(input("Enter deposit amount: "))
                        print(f"New balance: {bank.deposit(account_number, amount)}")
                    elif operation == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        print(f"New balance: {bank.withdraw(account_number, amount)}")
                    elif operation == "3":
                        print(bank.delete_account(account_number))  # Delete the account
                        break
                    elif operation == "4":
                        break
                    else:
                        print("Invalid operation choice.")
            else:
                print("Invalid account number.")
        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()