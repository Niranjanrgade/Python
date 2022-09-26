# Circle class
# 1 - Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the
# constructor:
# def init (self,a,b,r):
# self.a = a
# self.b = b
# self.r = r
# A:- Define a Area() method of the class which calculates the area of the circle.
# B:-Define a Perimeter() method of the class which allows you to calculate the perimeter of
# the circle.


from math import pi

centre_x = int(input("Enter the X ordinate of centre of circle: "))
centre_y = int(input("Enter the Y ordinate of centre of circle: "))
radius = float(input("Enter the radius of circle: "))


class Circle:
    def __init__(self, centre_x, centre_y, radius):
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


circle = Circle(centre_x, centre_y, radius)

area = circle.area()
print(f"Area of the circle is {area}")

perimeter = circle.perimeter()
print(f"perimeter of the circle is {perimeter}")




