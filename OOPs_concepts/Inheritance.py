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