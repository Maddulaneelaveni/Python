# SCOPE : A variable is only available from inside the region it is created. This is called scope.
# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# Example of local scope:
def my_function():
    x = 10  # x is a local variable
    print(x)
my_function()  # Output: 10
# print(x)  # This will raise an error because x is not defined outside the function
