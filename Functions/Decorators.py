# What is a Decorator? 
# A decorator is a function that modifies the behavior of another function without changing its code.
# Real-life analogy:
# Think of a function as a gift .
# A decorator is the gift wrapper — it adds something extra without touching what’s inside.

# In Python, decorators are often used to add functionality to functions or methods in a clean and reusable way. 
# They can be used for logging, access control, memoization, and more.

# Why use decorators?
# Code Reusability: Decorators allow you to reuse code across multiple functions without modifying their code.
# Separation of Concerns: They help separate the core logic of a function from additional features like logging or timing.
# Clean Syntax: Using the @decorator syntax makes it clear that a function is being decorated, improving readability.

# Syntax of a decorator:
# @decorator_function
# def some_function():
#     # function body

# Example of a simple decorator that logs the execution time of a function:
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")  # Print execution time
        return result  # Return the result of the original function
    return wrapper
@timer
def example_function():
    time.sleep(2)  # Simulate a time-consuming task
example_function()  # Output: example_function executed in 2.0000 seconds
# In this example, the timer decorator wraps the example_function, measuring and printing how long it takes to execute.

# Decorators can also be used to add functionality to functions without modifying their code. 
# For example, you can create a decorator that adds logging to a function:
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper




