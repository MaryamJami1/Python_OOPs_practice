"""Create an abstract class Shape with an abstract method area().
Then create 2 subclasses: Rectangle and Circle.
Each subclass should implement its own area() method.

Rectangle area = length × width

Circle area = π × radius² (π = 3.14)"""

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rectangle_area = self.length * self.width
        return rectangle_area



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = 3.14 * self.radius * self.radius
        return circle_area
    


shape1 = Rectangle(20, 10)
shape2 = Circle(2)

print(shape1.area())
print(shape2.area())

      
