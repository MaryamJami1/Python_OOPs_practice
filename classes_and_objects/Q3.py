"""Create a class called Calculator with two numbers.
Add methods add(), subtract(), multiply() and divide()."""

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2

    def multi(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2   
    

c1 = Calculator(50, 20)   
print("Addition = ", c1.add())
print("Subtraction = ", c1.sub())
print("Multiplication = ", c1.multi())
print("Divide = ", c1.divide())

