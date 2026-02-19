# SCOPE : A variable is only available from inside the region it is created. This is called scope.
#   OR
# Scope = The region where a variable is accessible.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# Example of local scope:
def my_function():
    x = 10  # x is a local variable
    print(x)
my_function()  # Output: 10
# print(x)  # This will raise an error because x is not defined outside the function

# Global Scope
# A variable created in the main body of the code is a global variable and belongs to the global scope. Global variables can be used by everyone, both inside and outside of functions.
# Example of global scope:
x = 10  # x is a global variable
def my_function():
    print(x)  # x can be accessed inside the function
my_function()  # Output: 10
print(x)  # Output: 10

# Enclosing Scope
# A variable created inside a function is in the local scope of that function, but if there is a nested function, the inner function can access the variables of the outer function. This is called enclosing scope.
# Example of enclosing scope:
def outer_function():
    x = 10  # x is in the local scope of outer_function
    def inner_function():
        print(x)  # x can be accessed in inner_function because of enclosing scope
    inner_function()  # Output: 10
outer_function() # Output: 10

# Built-in Scope
# A variable created in the built-in scope is a built-in variable and belongs to the built-in scope. Built-in variables are available in any part of the code.
# Example of built-in scope:
print(len("Hello"))  # len is a built-in function, so it can be used anywhere in the code

# Python follows the LEGB Rule:
# L - Local - Inside current function
# E - Enclosing - Inside outer function
# G - Global - At the top-level of the module (module-level)
# B - Built-in - Python's built-in names (len, sum, print, etc.)
# Local → Enclosing → Global → Built-in -> This is the order in which Python looks for a variable when it is referenced. It first looks in the local scope, then in the enclosing scope, then in the global scope, and finally in the built-in scope.

# 👍 Must Remember :

# LEGB rule - Python searches for variables in this order: Local → Enclosing → Global → Built-in, and stops when it finds the first match.
# This ensures predictable and structured variable resolution.

# UnboundLocalError reason - If you assign a variable inside a function, Python treats it as local, even if a global variable exists.
#So trying to use it before assignment causes UnboundLocalError.

# nonlocal vs global  : 
# global: Used to modify a variable defined at the module (global) level.
# nonlocal: Used to modify a variable in the nearest enclosing function, not the global scope.

# Late binding problem - Python looks up variable values when the function is called, not when it is created.
# So loop variables in closures all refer to the final value unless fixed.

# Closure concept

# Mutable default argument trap

# Class scope ≠ enclosing scope

# List comprehension scope (Python 3)