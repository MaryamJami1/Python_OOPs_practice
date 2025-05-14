"""Create a class Laptop with brand and price. Show brand and price using a method.
 Add a destructor that prints "Laptop object deleted"."""


class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


    def showDetails(self):
        return f"brand {self.brand} price {self.price}"
    

    def __del__(self):
        print("Laptop object deleted")



lap1 = Laptop("lenovo", "60,000")   
print(lap1.showDetails())






