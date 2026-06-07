# The Problem: Banking Account Management System
# Scenario
# You need to design a backend component for a bank. The bank offers two types of accounts: Savings Account and Current Account. Both accounts share some common features but have different rules for withdrawals and interest.

# Requirements
# Base Class (Account):

# Attributes: account_number (string), account_holder (string), and _balance (float, protected/private attribute initialized to 0.0).

# Methods:

# deposit(amount): Adds money to the balance.

# withdraw(amount): Abstract-like behavior (to be overridden), but should check if funds are sufficient.

# get_balance(): A getter method to safely view the balance.

# Derived Class 1 (SavingsAccount):

# Inherits from Account.

# Additional Attribute: interest_rate (float, e.g., 0.04 for 4%).

# Override withdraw(amount): A savings account cannot have a balance drop below a minimum maintenance fee of $100. If a withdrawal pushes the balance below $100, deny it.

# New Method add_interest(): Calculates interest based on the current balance and adds it to the balance.

# Derived Class 2 (CurrentAccount):

# Inherits from Account.

# Additional Attribute: overdraft_limit (float, e.g., $500).

# Override withdraw(amount): A current account allows the balance to go negative, up to the specified overdraft_limit. (e.g., If balance is $100 and limit is $500, they can withdraw up to $600).

class Account:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        # Encapsulation: Using a single underscore to denote a protected variable
        self._balance = float(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New Balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        # Base rule for withdrawal
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdrew ${amount}. Remaining Balance: ${self._balance}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def get_balance(self):
        return self._balance


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, initial_balance=0.0, interest_rate=0.04):
        # Call the parent constructor
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate = interest_rate
        self.min_balance = 100.0

    # Method Overriding
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False
        
        # Check if withdrawal violates the minimum balance rule
        if self._balance - amount >= self.min_balance:
            self._balance -= amount
            print(f"[Savings] Withdrew ${amount}. Balance: ${self._balance}")
            return True
        else:
            print(f"[Savings] Transaction Denied! Must maintain minimum balance of ${self.min_balance}")
            return False

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest of ${interest} added. New Balance: ${self._balance}")


class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, initial_balance=0.0, overdraft_limit=500.0):
        super().__init__(account_number, account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit

    # Method Overriding
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False
        
        # Check if withdrawal is within the overdraft limit
        if self._balance - amount >= -self.overdraft_limit:
            self._balance -= amount
            print(f"[Current] Withdrew ${amount}. Balance: ${self._balance}")
            return True
        else:
            print(f"[Current] Transaction Denied! Exceeds overdraft limit of ${self.overdraft_limit}")
            return False


# --- Driver Code to Test Polymorphism ---
if __name__ == "__main__":
    print("--- Testing Savings Account ---")
    sav = SavingsAccount("SAV123", "Alice", initial_balance=500)
    sav.deposit(100)       # Balance: 600
    sav.withdraw(550)      # Denied (600 - 550 = 50, which is < 100)
    sav.withdraw(200)      # Allowed. Balance: 400
    sav.add_interest()     # 400 * 0.04 = 16. New Balance: 416

    print("\n--- Testing Current Account ---")
    curr = CurrentAccount("CURR789", "Bob", initial_balance=200)
    curr.withdraw(300)     # Allowed (Balance goes to -100, within -$500 limit)
    curr.withdraw(500)     # Denied (-100 - 500 = -600, exceeds limit)