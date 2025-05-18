"""Overload the __sub__() operator in a class
 Point to subtract one point from another and print result using __str__()."""

class Subtraction:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2


    def __sub__(Sub1, Sub2):
        return Subtraction(Sub1.val1 - Sub2.val1, Sub1.val2 - Sub2.val2)
    

    def __str__(self):
        return f"Subtaction = {self.val1} , {self.val2}"
  
Sub1 = Subtraction(20, 10)
Sub2 = Subtraction(10, 5)
newSub = Sub1 - Sub2

print(newSub)

# print(f"{Sub1.val1} - {Sub2.val1} = {newSub.val1}")
# print(f"{Sub1.val2} - {Sub2.val2} = {newSub.val2}")



        