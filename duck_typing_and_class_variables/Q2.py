"""Create a class Car with a class variable wheels = 4. 
Each Car object has its own color instance variable.
Create 3 car objects with different colors and
 print their colors and number of wheels using both instance and class name."""

class Car:
    wheels = 4

    def __init__(self, color):
        self.color = color


car1 = Car("green")
car2 = Car("silver")
car3 = Car("white")

print(f"car 1 color {car1.color} and wheels are {Car.wheels}")
print(f"car 2 color {car2.color} and wheels are {Car.wheels}")
print(f"car 3 color {car3.color} and wheels are {Car.wheels}")



"""print(Car.wheels) ## it can access because its own var of class
print(car1.wheels) ## this is class var but can access using obj name
print(Car.color) ##  this is intance var it can't access using class name

car3.color = "black" ## object can reassign their var values
print(f"car 3 color {car3.color} and wheels are {Car.wheels}")

car1.wheels = 6 ## object can't reassign class var value its create new instance variable.
print(car1.wheels)
print(Car.wheels)

Car.wheels = 8 ## change value of class var like this
print(Car.wheels)"""