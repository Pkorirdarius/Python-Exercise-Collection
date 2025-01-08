# Define the Account class and its attributes as specified above.
class Account:
    """
    Account class to take in user details and ensure uniqueness of each bank account.
    """
    # variable to keep track of the last assigned account number
    previous_account_number = 1000
    
    def __init__(self,user_name,date_of_birth,password):
        self.date_of_birth = date_of_birth
        self.account_balance = 0.0
        self.account_holder = user_name
        self.password = password
        # Generate a unique account number for each new account
        Account.last_account_number += 1
        self.account_number = Account.last_account_number
        # Define the deposit() method. It should take in one argument, the amount to be deposited, and add it to the account balance.
    def deposit(self,deposit_amount):
        new_balance = self.account_balance + deposit_amount
        print(f"Successfully deposited {deposit_amount}. New bank account balance : Ksh{new_balance}")
        # Define the withdraw() method. It should take in one argument, the amount to be withdrawn, and subtract it from the account balance. The method should only execute the withdrawal if the account balance is greater than or equal to the amount to be withdrawn.
    
    def withdraw(self,withdraw_amount,password):
        if password != self.password:
            print("Incorrect password. Withdrawal denied.")
            return
        if self.account_balance >= withdraw_amount:
            self.account_balance -= withdraw_amount
            print(f"Successfully withdrew {withdraw_amount} new bank balance is ksh{self.account_balance}")
        else:
            print(f"Insufficient funds you cannot withdraw Ksh{withdraw_amount}")
            
            # Define the check_balance() method. It should return the current account balance.
    def check_balance(self):
        print(f"You bank account balance is Ksh{self.account_balance}")

