#class method
"""Create a class School with a class variable school_name = "ABC School". 
Write a class method change_name(cls, new_name) that updates the school name."""

class School:
    school_name = "ABC School"

    @classmethod
    def change_name(cls, new_name):
        print(cls.school_name)
        cls.school_name = new_name
        print(cls.school_name)


school = School()
school.change_name("XYZ School")



#uses of cls
"""
class HighSchool(School):
    school_name = "Old school"

highStudent = HighSchool()
highStudent.change_name("High School")
"""