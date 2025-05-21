"""Create a base class Animal with a class method create(cls) that returns an object of the class. 
Then create a subclass Cat, and use Cat.
create() to create an object and print its type."""

class Animal:
    @classmethod
    def create(cls):
        return cls()
    

class Cat(Animal):
    pass


class Use_Cat(Animal):
    pass


cat = Cat().create()
useCat = Use_Cat().create()


print(type(cat))
print(type(useCat))

