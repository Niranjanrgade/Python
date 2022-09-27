# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
# Write a python program to Create a child class Bus that will inherit all
# of the variables and methods of the Vehicle class


# Base/ super/ parent class
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_details(self):
        print(f"The maximum speed of the vehicle is {self.max_speed}")
        print(f"The mileage of the vehicle is {self.mileage}")


# Derived/ sub/ child class
class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        Vehicle.__init__(self, max_speed, mileage)


# Derived/ sub/ child class instance
bus = Bus(70, 25)

# Method call of Base /super /parent class method using Derived/ sub/ child class instance
bus.print_details()

