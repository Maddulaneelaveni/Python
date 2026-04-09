# What is Abstraction?
# Abstraction is an OOP concept where we hide internal implementation details and show only essential features to the user.
# It allows us to focus on what an object does rather than how it does it.
# In Python, we can achieve abstraction using abstract classes and methods from the `abc` module.
from abc import ABC, abstractmethod


# PROBLEMS ON ABSTRACTION

# Problem 3: Create an Abstract Class
# Create an abstract class Shape with:
# * abstract method area()
# * abstract method perimeter()
# Then create:
# * Circle
# * Rectangle

# 1. We want to create a system for different types of shapes (Circle, Rectangle, etc.) where each shape has its own way of calculating area and perimeter.

from abc import ABC, abstractmethod
import math
# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
# Circle Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
# Rectangle Class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
c = Circle(5)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())
r = Rectangle(4, 6)
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())
