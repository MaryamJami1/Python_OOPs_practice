"""Create two classes Shape and Circle. Override a method area() in Circle. 
Show polymorphism using a parent reference."""

class Shape:
    def area(self):
       print ("area from shape")


class Circle(Shape):
    def area(self):
        # super().area()
        return "area from circle"
    

area = Circle()
print(area.area())
