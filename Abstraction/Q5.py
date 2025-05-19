"""Create an abstract class PaymentMethod with abstract methods:
authenticate_user() make_payment(amount)
Then create two concrete classes:CreditCard PayPal
Each class should:Implement both abstract methods
Simulate the payment flow with custom print statements"""

from abc import ABC , abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def authenticate_user(self, *args , **kwargs):
        pass


    @abstractmethod
    def make_payment(self, amount):
        pass



class Credit(PaymentMethod):
    def authenticate_user(self, name , pin):
        print(f"Authenticate user is {name} and the pin is {pin} ")
        print("Credit card authentication successful.")
        

    def make_payment(self, amount):
        print(f"Processing credit card payment of ${amount}...")
        print("Credit card payment completed.")




class Paypal(PaymentMethod):
    def authenticate_user(self, email):
        print(f"Authenticating PayPal user with email {email}...")
        print("PayPal authentication successful.")

    def make_payment(self, amount):
       print(f"Processing PayPal payment of ${amount}...")
       print("PayPal payment completed.")
        


