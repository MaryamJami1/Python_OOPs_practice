"""Create a class Person with method introduce(). 
Inherit it into class Student, override the method to show “Im a student”."""


class Person:
    # Method to introduce a generic person
    def introduce(self):
        return "Hello from parent"


class Student(Person): # Child class Student inheriting from Person
  
    def introduce(self):   # Overriding the introduce() method from the parent class
        return "Hello from student"
 
 
# Calling the introduce() method
# Since this is a Student object, it will call the overridden method
st1 = Student()
print(st1.introduce())
