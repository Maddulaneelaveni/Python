#  1. Class and Object
# Define a class named Student
class Student:
    # Constructor to initialize object attributes
    def __init__(self, name, age, marks):
        self.name = name      # Store student's name
        self.age = age        # Store student's age
        self.marks = marks    # Store student's marks

    # Method to display student details
    def display(self):
        print(self.name, self.age, self.marks)  # Print all attributes

# Create 3 objects (instances of Student class)
s1 = Student("Neelaveni", 21, 85)
s2 = Student("B", 22, 90)
s3 = Student("C", 20, 88)

# Call display method for each object
s1.display()
s2.display()
s3.display()

# 2. Constructor
# # Define Employee class
class Employee:
    # Constructor to initialize values when object is created
    def __init__(self, name, department, salary):
        self.name = name              # Store employee name
        self.department = department # Store department
        self.salary = salary         # Store salary
    # Method to display employee details
    def show_details(self):
        print(self.name, self.department, self.salary)
# Create objects
e1 = Employee("Neelaveni", "IT", 50000)
e2 = Employee("Anu", "HR", 40000)
# Display details
e1.show_details()
e2.show_details()

# 3.Encapusalation
class BankAccount:
    def __init__(self):
        self.__balance = 0   # Private variable (cannot be accessed directly)
    # Method to add money
    def deposit(self, amount):
        self.__balance += amount   # Increase balance
    # Method to withdraw money
    def withdraw(self, amount):
        self.__balance -= amount   # Decrease balance
    # Method to check balance
    def check_balance(self):
        print("Balance:", self.__balance)
acc = BankAccount()
acc.deposit(1000)
acc.withdraw(200)
acc.check_balance()

# 4.Single Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name   
        self.age = age     
    def display(self):
        print(self.name, self.age)  
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)  
        self.marks = marks          
s = Student("Neelaveni", 21, 85)
s.display()
print("Marks:", s.marks)

# 5. Multilevel Inheritance 
class Animal:
    def eat(self):
        print("Eating")   
class Dog(Animal):
    def bark(self):
        print("Barking")  
class Puppy(Dog):
    def weep(self):
        print("Weeping") 
p = Puppy()
p.eat()   
p.bark()  
p.weep()  


# 6. Encapsulation (Validation Example)
# Create class Student
# Private variable: marks
# Create method: set_marks()
# Condition: Marks should not be negative.
# Create method: get_marks()

class Student:
    def __init__(self):
        self.__marks = 0  # Private variable

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks cannot be negative")

    def get_marks(self):
        return self.__marks

s = Student()
s.set_marks(85)
print("Marks:", s.get_marks())

s.set_marks(-10)  # Invalid case