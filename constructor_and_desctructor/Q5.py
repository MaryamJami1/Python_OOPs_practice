"""Create a class Product with name, category, and price. 
Create 2 objects and show their details using a method."""


class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def show_details(self):
        return f"Item is {self.name} in category of {self.category} and price is {self.price}"


product1 = Product("Fan", "Electronic", "10,000")      
print(product1.show_details()) 

product2 = Product("Plate" , "Crockery", "500")
print(product2.show_details())