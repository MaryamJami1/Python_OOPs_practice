"""Create a class BankAccount with:Public attribute: account_holder
Protected attribute: _balance
Private attribute: __pin
Write a method to show balance and pin."""

class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder # Public attribute
        self._balance = balance # Protected attribute
        self.__pin = pin # Private attribute


    def show_details(self):
     return f"Account Holder: {self.account_holder}, Balance: {self._balance}, PIN: {self.__pin}"    

acc1 = BankAccount("maryam", "800000", "176890")       
print(acc1.show_details())
# print(acc1._balance) # this will access but not recommended because it is protected attribute it should be used within the class or subClass
# print(acc1.__pin) # this will throw an error because it is private attribute
# print(acc1._BankAccount__pin) # this will access the private attribute but not recommended this process is called name mangling

