"""Create class Shape with method area(). 
Override it in child class Circle to calculate area of a circle using radius."""


class Shape:
    def area(self):
        print ("area method from shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.1416 * self.radius * self.radius
        print(area)
      
circle = Circle(5)
circle.area()