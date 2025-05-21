"""Create a class MathTools with a static method 
add(x, y) that returns the sum of two numbers. 
It should not depend on class or instance data."""

class MathTools:
    @staticmethod
    def add(x, y):
        return x + y
    

print(MathTools.add(10, 28))