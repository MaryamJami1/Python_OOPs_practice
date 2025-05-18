"""Create an abstract class Employee with an abstract method calculate_salary().
Then create 2 classes:

FullTimeEmployee (salary is fixed)

PartTimeEmployee (salary = hourly rate × hours worked)"""

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass



class FullTimeEmployee(Employee):
    def __init__(self):
       self.salary = 5000

    def calculate_salary(self):
       return self.salary 



class PartTimeEmployee(Employee):
    def __init__(self, hourlyRate, hoursWork):
        self.hourlyRate = hourlyRate
        self.hoursWork = hoursWork

    def calculate_salary(self):
        salary = self.hourlyRate * self.hoursWork
        return salary
        


full_time_employee = FullTimeEmployee()
Part_time_employee = PartTimeEmployee(500, 5)


print(full_time_employee.calculate_salary())
print(Part_time_employee.calculate_salary())
