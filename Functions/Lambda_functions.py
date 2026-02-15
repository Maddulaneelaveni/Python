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

# Sort List of Tuples
points = [(1, 2), (3, 1), (5, 4)]
points.sort(key=lambda point: point[1])
print(points)  # Output: [(3, 1), (1, 2), (5, 4)]

# Use with map() to square a list of numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Use with filter() to get even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Use with sorted() to sort a list of strings by their length
strings = ["apple", "banana", "kiwi", "grapefruit"]
sorted_strings = sorted(strings, key=lambda s: len(s))
print(sorted_strings)  # Output: ['kiwi', 'apple', 'banana', 'grapefruit']

#  Lambda functions are a powerful tool for creating small, one-off functions without the need for a formal function definition. 
# They are especially useful in situations where you need to pass a simple function as an argument to higher-order functions like map(), filter(), and sorted().

# Use reduce() with Lambda . Find the product of all numbers in a list.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Sort Dictionary by Values
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)  # Output: {'banana': 1, 'cherry': 2, 'apple': 3}

# Find Longest Word in List
words = ["apple", "banana", "kiwi", "grapefruit"]
longest_word = max(words, key=lambda w: len(w))
print(longest_word)  # Output: 'grapefruit'





