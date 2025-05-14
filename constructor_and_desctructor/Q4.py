"""Create a class BankAccount with __init__() to set account number and balance.
 Use __del__() to print a message like “Account closed.”"""



class BankAccount:
    def __init__(self, AccNo, Balance):
        self.AccNo = AccNo
        self.Balance = Balance


    def __del__(self):
        print("Account Closed")

acc1 = BankAccount("09890", "30,000")
