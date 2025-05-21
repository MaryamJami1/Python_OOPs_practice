#instance method
""" Create a class Student with instance variables name and grade.
Write an instance method promote() that increases the grade by 1."""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def promote(self):
      self.grade += 1
      print(f"Student name: {self.name} promote in garde: {self.grade}")


Student1 = Student("Sara",5)
Student1.promote()