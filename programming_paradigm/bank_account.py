# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize account with optional initial balance (default = 0)."""
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit amount into account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw amount from account if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Prints the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
