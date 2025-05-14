"""Create a class called Dog with attributes name and breed.
 Add methods bark() and sit()."""

class Dog:
    def __init__(self, name:str, breed:bool):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking {self.name} has breed? {self.breed}")     

    def sit(self):
        print(f"{self.name} is sitting {self.name} has breed? {self.breed}")      


dog1 = Dog("tommy", True )
dog1.bark()


dog2 = Dog("shoofy" , False)
dog2.sit()