import math

# Base class
class Shape:
    def area(self):
        print("Area method not implemented.")


# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Triangle subclass
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Using the classes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())
print("Triangle Area:", triangle.area())
