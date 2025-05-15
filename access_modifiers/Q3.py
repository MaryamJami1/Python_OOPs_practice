"""Create a class Teacher with a private attribute __salary. 
Try to access it outside the class using name mangling."""


class Teacher:
    __salary = 800000  # Private class attribute

salary = Teacher()

# print(salary.__salary)  Error: can't access private attribute directly
print(salary._Teacher__salary)  #  Accessed using name mangling
