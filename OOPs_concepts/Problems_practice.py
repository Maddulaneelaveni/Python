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