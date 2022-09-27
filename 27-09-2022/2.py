# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and
# a Area() method to calculate the area of the rectangle.
# Create a method display() that display the length, width, perimeter and
# area of an object created using an instantiation on rectangle class.
# Create a Parallelepiped child class inheriting from the Rectangle class and with a height attribute and
# another Volume() method to calculate the volume of the Parallelepiped

print('*' * 85)
print(f"{'Welcome to Geometry program!':^85}")
print('*' * 85)

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))


# Base/ super/ parent class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print(f"Length of rectangle is {self.length}")
        print(f"Width of rectangle is {self.width}")
        print(f"Perimeter of the rectangle is {self.perimeter()}")
        print(f"Area of the rectangle is {self.area()}")


# Derived/ sub/ child class
class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def volume(self):
        return Rectangle.area(self) * self.height

    def display(self):
        Rectangle.display(self)
        print(f"Height of the Parallelepiped is {self.height}")
        print(f"Volume of the Parallelepiped is {self.volume()}")


choice = input("Press R for Rectangle, P for Rectangle and Parallelepiped: ")

if choice == 'R' or choice == 'r':
    # Instance of Base/ super/ parent class
    rectangle = Rectangle(length, width)
    rectangle.display()


elif choice == 'P' or choice == 'p':
    height = float(input("Enter the height of Parallelepiped: "))
    # Instance of Derived/ sub/ child class
    parallelepiped = Parallelepiped(length, width, height)
    parallelepiped.display()

else:
    print("Enter valid choice!")

print('*' * 85)


