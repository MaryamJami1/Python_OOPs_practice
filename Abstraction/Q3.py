"""Create an abstract class BankAccount with an abstract method withdraw(amount).
Then create 2 classes:

SavingsAccount (withdraw only allowed if balance ≥ amount)

CurrentAccount (allow overdraft up to a certain limit)"""


from abc import ABC , abstractmethod


class BankAccount(ABC):

    @abstractmethod
    def withdraw_amount(self):
        pass


class SavingAccount(BankAccount):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def withdraw_amount(self):
        if self.balance > self.amount:
            print(f"successfully withdrew your amount = {self.amount}")

        else:
            print("sorry balance is insufficent")
            
        
        

class CurrentAccount(BankAccount):
    pass