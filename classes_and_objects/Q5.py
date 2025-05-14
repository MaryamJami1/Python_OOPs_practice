"""Create a class called Mobile with brand and model. 
Create an object and print its brand and model using a method get_info()."""

class Mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


    def get_info(self):
        return f"Mobile brand is {self.brand} and model is {self.model}"
    

mob1 = Mobile("Apple", "iphone15")
print(mob1.get_info())
