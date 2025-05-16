"""Create 2 parent classes Writer and Reader, both with a method info(). 
Inherit them into class Blogger using multiple inheritance."""


class Writer:
    # Method info() defined in Writer class
    def info(self):
        return "hello from writer"


class Reader:
    # Method info() also defined in Reader class
    def info(self):
        return "hello from reader"

# Blogger class inherits from both Writer and Reader (Multiple Inheritance)
class Blogger(Writer, Reader):
    pass

blog1 = Blogger()

# Calling the info() method — since both parents have it,
# Python uses Method Resolution Order (MRO) and picks the first parent (Writer)
print(blog1.info())
