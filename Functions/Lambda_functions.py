# Lamda Funstions :
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.

# Why use lambda functions?
# Concise syntax for simple functions
# Useful for short-term use (e.g., in map(), filter(), sorted())
# Can be defined inline without needing a formal function definition

# Syntax of lambda function:
# lambda arguments: expression

# Example of lambda function:

# Add 10 to argument a, and return the result:
x = lambda a: a + 10
print(x(5))  # Output: 15

# Multiply argument a with argument b and return the result:
y = lambda a, b: a * b
print(y(5, 3))  # Output: 15

# Use lambda function with map() to square each number in a list:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]




