# SCOPE : A variable is only available from inside the region it is created. This is called scope.

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