"""Make a class Employee that takes name, age, and department in constructor. 
Add a method details() to show employee info."""

class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def details(self):
       return f"employee name is {self.name}, age is {self.age} and department is {self.department}"
        

employee1 = Employee("Hassan" , "28" , "Finance" )
print(employee1.details())
