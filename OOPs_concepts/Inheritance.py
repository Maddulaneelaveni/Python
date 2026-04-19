# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass) to inherit properties and behaviors (attributes and methods) from an existing class (called a parent or superclass). 
# This promotes code reusability and establishes a natural hierarchical relationship between classes.
# It helps in:
# Code reusability
# Reducing redundancy
# Creating a hierarchical relationship

# Basic Syntax:
class Parent:
    def show(self):
        print("This is parent class")
class Child(Parent):
    def display(self):
        print("This is child class")
obj = Child()
obj.show()      # inherited method
obj.display()   # child class method
# In the above example, the Child class inherits from the Parent class, allowing it to use the show() method defined in the Parent class. The Child class can also have its own methods, such as display().
# Output:
# This is parent class
# This is child class

# Types of Inheritance:

# 1. Single Inheritance: One child inherits from one parent.
class A:
    def method_A(self): # This is the parent class method
        print("Class A") # This is the parent class
class B(A):
    def method_B(self): # This is the child class method
        print("Class B") # This is the child class that inherits from class A












class Animal:
    def eat(self):
        print("Eating")
    def sleep(self):
        print("Sleeping")
class Dog(Animal):   
    def bark(self):
        print("Barking")
d = Dog()
d.eat()  
d.sleep()  
d.bark()  