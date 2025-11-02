# Function
# A function is a block of code that performs a specific task and can be reused multiple times.
# Instead of writing the same logic repeatedly, we define it once and call it multiple times.

#In Python, functions help in:
# Code reusability
# Modularity
# Better readability
# Easier debugging

# Syntax:
def function_name(parameters):
    # function body
    return value

# Example:
def greet():
    print("Hello, Neelaveni!")

# we use greet() to call the function

# Function Components:

# 1.def: Keyword to define a function.
# 2. function_name : Identifier to call the function later.
# parameters: Variables that receive input values
# 4. function body: Indented block of code that performs the task.
# 5. docstring (Optional): description of the function's purpose.
# 6. return (Optional): statement to send back a value to the caller.


# Parameters vs Arguments:

# parameters are variables listed inside parentheses in the function definition.

# Arguments are the actual values passes when calling the function.

# Example:
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")
greet("Neelaveni")  # "Neelaveni" is an argument



# Types of Arguments

# 1. Positional Arguments: Passed in the order defined.(oreder matters)
def student(name, age):
    print(name, age)
student("Neelaveni", 20)  

# 2. Keyword Arguments: Passed using parameter names (order doesn't matter)
student(age=20, name="Neelaveni")

# 3. Default Arguments: Parameters with default values if no argument is provided.
def student(name, age=18):
    print(name, age)
student("Neelaveni")  # uses default age
student("Mokshi", 20)  # overrides default age

# 4. Variable-length Arguments: Accepts arbitrary number of arguments using *args and **kwargs
# *args : for multiple positional arguments
# **kwargs : for multiple keyword arguments

def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, name="Viswanath", role="Data Analyst")

# Return Statement
# The return keyword is used to exit a function and return a value to the caller.
# If no return is specified, the function returns None by default.

def add(a, b):
    return a + b

result = add(10, 5)
print(result)



# Scope and Lifetime of Variables

# Local variables → declared inside a function
# Global variables → declared outside all functions