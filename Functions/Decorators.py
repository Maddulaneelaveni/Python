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
