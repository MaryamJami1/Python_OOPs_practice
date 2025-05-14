"""Create a class called Student that takes name and roll_no using a constructor. 
Print the student info using a method show_info()."""

class Student:
    def __init__(self, rollNo, name):
        self.rollNo = rollNo
        self.name  = name

    def show_info(self):
        print(f"Student name is {self.name}, rollNo is {self.rollNo}")       


stdnt1 = Student("Maryam" , 176176) 
stdnt1.show_info()     

