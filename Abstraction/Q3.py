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

    def __init__(self, balance, amount, overdraft_limit):
     self.balance = balance
     self.amount = amount
     self.overdraft_limit = overdraft_limit

    def withdraw_amount(self):
     if self.balance - self.amount >= -self.overdraft_limit:
        self.balance -= self.amount
        print(f"Withdraw successful. New balance: {self.balance}")
     else:
        print("Withdraw failed. Overdraft limit exceeded")



saving = SavingAccount(5000, 4000)
saving.withdraw_amount()


current = CurrentAccount(5000, 6000, 2000)
current.withdraw_amount()