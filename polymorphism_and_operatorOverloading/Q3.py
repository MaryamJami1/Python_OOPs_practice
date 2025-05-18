"""Create a class Vector(x, y).
 Overload the + operator to add two vectors and return a new vector."""


class Vector:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2


    def __add__(add1 , add2):
        return Vector(add1.val1 + add2.val1 ,add1.val2 + add2.val2)
    

    def __str__(self):
        return f"NewVector {self.val1} {self.val2}"

        
add1 = Vector(25, 40)
add2 = Vector(10, 50)

newVec = add1 + add2

print(newVec)




