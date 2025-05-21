# Mixed Methods
"""Create a class Account with:Instance variables: owner, balance
An instance method deposit(amount) that adds to the balance
A class variable bank_name = "UBL"
A class method change_bank(cls, name) to change the bank name
A static method bank_info() that prints "Banks are important institutions."""

class Account:
    bank_name = "UBL"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def  deposit(self, amount):
        self.balance += amount
        print(f"{amount} amount added to the acount Your current balance is: {self.balance}")

   

    @classmethod
    def change_bank(cls, name):
        print(f"OLD Bank name: {cls.bank_name}")
        cls.bank_name = name
        print(f"NEW Bank name: {cls.bank_name}")



    @staticmethod
    def bank_info():
        print("Banks are important institutions.")



bank = Account("Maryam", 20000)
bank.deposit(30000)

bank.change_bank("Islamic Bank")

Account.bank_info()