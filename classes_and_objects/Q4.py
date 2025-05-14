"""Create a class called Fan with attributes speed and brand. 
Add a method increase_speed() which increases speed by 10."""


class Fan:
    def __init__(self, speed, brand):
        self.speed = speed
        self.brand = brand


    def increase_speed(self):
       print(f"Default speed is {self.speed} RMP and Brand is {self.brand}")
       self.speed += 10
       return f"After Increase by 10 Fan speed is {self.speed} RPM"



fan1 = Fan(50,"starco" )
print(fan1.increase_speed())