"""Create an abstract class Vehicle with an abstract method start().
Create classes Bike and Truck that override the start() method.
Each start() method should print its own logic."""



from abc import ABC , abstractmethod

class Vechile(ABC):

    @abstractmethod
    def start(self):
         pass
    

class Bike(Vechile):
     def start(self):
          print ("Kick start the bike")


class Truck(Vechile):
     def start(self):
         print("Turn the key to start the truck")


bike = Bike()
bike.start()

truck = Truck()
truck.start()
