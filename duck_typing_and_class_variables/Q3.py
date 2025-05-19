"""Create two classes, Dog and RobotDog. 
Both have a method speak() returning "Woof" and "Electronic Woof", respectively.
Add a class variable species = "Canine" to both classes.
Write a function introduce_pet(pet) that prints the species and calls speak().
Test the function with objects from both classes."""


from abc import ABC , abstractmethod
class Pet(ABC):
    @abstractmethod
    def speak():
        pass
    

class Dog(Pet):
    species = "Canine"
    def speak(self):
        return "woof"
    
class RobotDog(Pet):
    species = "Canine"
    def speak(self):
        return "Electronic Woof"


def introduce_pet(pet):
    print(pet.species)
    print (pet.speak())


dog = Dog()
robotDog = RobotDog()

introduce_pet(dog)
introduce_pet(robotDog)