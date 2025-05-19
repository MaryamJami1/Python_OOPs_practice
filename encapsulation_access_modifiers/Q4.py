"""Create a class Car with:
Public attribute brand
Protected method _engine_start()
Call protected method from a child class ElectricCar."""


class Car:
    def __init__(self, brand):
        self.brand = brand  # Public attribute

    def _engine_start(self):  # Protected method (by convention)
        return f"{self.brand} engine start...."

# Child class ElectricCar inheriting from Car
class ElectricCar(Car):
    def start(self):  # Public method to access protected method
        return self._engine_start()  # Calling protected method from parent class


car1 = ElectricCar("tesla") # this data recieve in parent class brand attribute because if constructor not define in child class python will automatically pass the data to the parent

# Calling the start method which internally calls the protected method
print(car1.start())  # Output: tesla engine start....

