"""Create a class Phone and a subclass Smartphone. 
Use single inheritance and call parent constructor using super()."""

class Phone:
    def __init__(self):
        print ("Hello from Phone")
     


class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
      
    

mobile = SmartPhone()

