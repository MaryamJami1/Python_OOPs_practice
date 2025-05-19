"""Create two classes, Cat and Robot. Both should have a method make_sound() — 
for Cat it returns "Meow", and for Robot it returns "Beep".
Write a function animal_sound(animal) that takes any object and 
calls its make_sound() method (without checking its type).
Test it with objects of both classes."""


class Cat:
    def make_sound(self):
        print("Meow!")


class Robot:
    def make_sound(self):
        print("Beep!")


def animal_sound(animal):
    animal.make_sound()


cat = Cat()
robot = Robot()

animal_sound(cat)
animal_sound(robot)