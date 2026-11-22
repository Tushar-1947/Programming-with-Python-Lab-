from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)

print("Circle Area:", round(circle.area(), 2))
print("Rectangle Area:", rectangle.area())
print("Triangle Area:", triangle.area())

print("\n--- Operator Overloading ---")
print("Circle + Rectangle:", round(circle + rectangle, 2))
print("Rectangle - Triangle:", rectangle - triangle)
print("Circle + Triangle:", round(circle + triangle, 2))