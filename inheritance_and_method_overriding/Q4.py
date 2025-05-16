"""Use super() in a child class Employee to call
 parent class Person's __init__() which sets the name and age."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


employ1= Employee("maryam", 20)
print(f"Name: {employ1.name} Age: {employ1.age}" )
