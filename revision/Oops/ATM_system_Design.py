from abc import ABC, abstractmethod

class BankAccount:

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposit ₹{amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print(f"Withdraw ₹{amount}")

    def get_balance(self):
        return self.__balance


class Transaction(ABC):

    def __init__(self, account):
        self.account = account

    @abstractmethod
    def execute(self, amount=0):
        pass


class Deposit(Transaction):

    def execute(self, amount):
        self.account.deposit(amount)


class Withdraw(Transaction):

    def execute(self, amount):
        self.account.withdraw(amount)


class CheckBalance(Transaction):

    def execute(self, amount=0):
        print(f"Current Balance: ₹{self.account.get_balance()}")


# Main
account = BankAccount("12345", 10000)

deposit = Deposit(account)
withdraw = Withdraw(account)
check_balance = CheckBalance(account)

deposit.execute(5000)
withdraw.execute(2000)
check_balance.execute()