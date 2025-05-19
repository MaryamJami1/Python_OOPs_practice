"""Create a class Student with a class variable school = "Old School". 
Create 2 student objects.
Change the class variable school to "New School" using the class name.
Print the school for both students before and after the change."""


class Student:
    school = "old school"



stdnt1 = Student()
stdnt2 = Student()

print(stdnt1.school)
print(stdnt2.school)

Student.school = "New School"

print(stdnt1.school)
print(stdnt2.school)
