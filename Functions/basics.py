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
# Variables defined inside a function are local to that function and cannot be accessed outside.

x = 10  # global
def show():
    y = 5  # local
    print(x + y)
show()  # 15

# To modify a global variable inside a function:
x = 10
def modify():
    global x
    x = x + 5

modify()
print(x)  # 15



# Nested Functions (Inner Functions)
# Functions defined inside other functions.
def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()
outer()
# output:
# Outer function
# Inner function

# Inner functions are often used for encapsulation and decorators.



# Lambda (Anonymous) Functions :

# Small, unnamed functions defined using the lambda keyword.

# Syntax: lambda parameters: expression
# Lambda functions are one-liners with no def or return.
# Used for quick operations.

# ex:
square = lambda x: x * x
print(square(6))
# output: 36

# Lambda with map() function

nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, nums))
print(doubled)
# output: [2, 4, 6, 8, 10]

# Lambda with filter() function:
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
# output: [2, 4]

# Lambda with reduce() function:
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(product)  # output: 120   



# Recursion:
# A function calling itself is recursive.

# ex:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # output: 120


# Common Function Examples:
# 1. Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(celsius_to_fahrenheit(25))  # output: 77.0

# 2. Check Prime Number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(11))  # output: True

