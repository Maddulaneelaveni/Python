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
@logger
def add(a, b):
    return a + b
result = add(5, 3)  # Output: Calling add with arguments (5, 3) and keyword arguments {}
print(result)  # Output: 8
# In this example, the logger decorator wraps the add function, printing the arguments it was called with before executing the original function.
# Decorators can also be used to modify the behavior of a function.
# For example, you can create a decorator that checks if the user is authenticated before allowing access to a function:
def requires_authentication(func):
    def wrapper(user, *args, **kwargs):
        if not user.is_authenticated:
            print("User is not authenticated. Access denied.")
            return None
        return func(user, *args, **kwargs)
    return wrapper
@requires_authentication
def view_profile(user):
    print(f"Viewing profile of {user.name}")   
# In this example, the requires_authentication decorator checks if the user is authenticated before allowing access to the view_profile function. If the user is not authenticated, it prints an access denied message and returns None. 
# In summary, decorators are a powerful tool in Python that allow you to modify the behavior of functions in a clean and reusable way. 
# They can be used for a variety of purposes, including logging, access control, and performance measurement.

# import functools
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Do something before calling the original function
#         result = func(*args, **kwargs)  # Call the original function
#         # Do something after calling the original function
#         return result  # Return the result of the original function
#     return wrapper

# Importing functools and using @functools.wraps(func) is important when creating decorators because it preserves the original function's metadata, such as its name, docstring, and other attributes.

# Basic Properties of Decorators:
# 1. They are functions that take another function as an argument and return a new function
# 2. They can be applied to any function, regardless of its signature
# 3. They can be used to modify the behavior of a function without changing its code 

