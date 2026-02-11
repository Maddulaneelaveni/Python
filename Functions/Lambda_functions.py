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

# Square of a Number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Check Even or Odd
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(5))  # Output: Odd
print(is_even(6))  # Output: Even

# Find Maximum of Two Numbers
max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))  # Output: 20




