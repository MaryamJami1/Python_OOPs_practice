"""Create a class Employee with method work().
 Create Manager and Developer subclasses that override work().
 Loop through a list of employees and call work()."""



class Employee:
    def work(self):
        print("employee work")



class Manager(Employee):
    def work(self):
        print("Manager work")



class Developer(Employee):
    def work(self):
        print("Developer work")



employee = Employee()
manager = Manager()
developer = Developer()

list1 = [employee, manager, developer]


for person in list1:
    person.work()

