"""Create two classes Painter and Driver. Inherit them into class ArtistDriver. 
Call a method from both parents."""



class Painter:
    def painter(self):
        print("painter")


class Driver:
    def driver(self):
        print("Driver")

# Child class inheriting from both Painter and Driver (Multiple Inheritance)
class ArtistDriver(Painter, Driver):
    
    # Method defined in child class to call both parent methods using super()
    def child(self):    
        super().painter()  # Calls the painter() method from the first parent in MRO (Painter)
        super().driver()   # Calls the driver() method, MRO still finds it in Driver

obj1 = ArtistDriver()

# Calling the method defined in child class which triggers both parent methods
obj1.child()
