# Lists:

# A list is a collection of items in Python.
#                 (or)
# A list in Python is a data structure that stores a collection of elements.

# Lists can hold different types of data (integers, strings, floats, even other lists).

# Lists are ordered, mutable, and allow duplicates.

# Lists can hold different types of data (integers, strings, floats, even other lists).

# Key Properties of Lists

# Ordered → Items have a fixed order (indexing starts at 0).

# Mutable → You can change elements after creating the list.

# Allows duplicates → Same value can appear multiple times.

# Heterogeneous → Different data types in the same list.


# 1. Creating a list:

# Empty list
my_list = []

# List of integers
numbers = [1, 2, 3, 4, 5]

# Mixed data types
mixed = [1, "hello", 3.14, True]

# Nested list (list inside list)
nested = [1, [2, 3], [4, 5]]


# 2.Accessing List Elements

fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple (first element, index 0)
print(fruits[1])   # banana
print(fruits[-1])  # cherry (negative index → last element)


# 3.Changing List Elements

fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'cherry']


# 4.Common List Operations

# Concatenation
a = [1, 2]
b = [3, 4]
print(a + b)   # [1, 2, 3, 4]

# Repetition
print(a * 3)   # [1, 2, 1, 2, 1, 2]

# Membership test
print(2 in a)      # True
print(5 not in a)  # True



