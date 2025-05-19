"""Create a class Animal with protected method _make_sound(). 
In subclass Dog, call this method."""


class Animal:
    def _make_sound(self):
      return "make a sound"

class Dog(Animal):
     def say(self):
         return f"please {self._make_sound()}"
    

animal = Dog()  
print(animal.say())       


