"""Create a class Vector(x, y).
 Overload the + operator to add two vectors and return a new vector."""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"



add1 = Vector(20, 50)
add2 = Vector(5, 10)


newVec = add1 + add2
print(newVec)