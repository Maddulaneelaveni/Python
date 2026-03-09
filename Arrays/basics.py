# Array : An array is a collection of elements stored in a continuous memory location.
# Arrays can be of fixed size (static arrays) or dynamic size (dynamic arrays).
# 1. Static Arrays: In static arrays, the size is defined at the time of declaration and cannot be changed during runtime.
# 2. Dynamic Arrays: In dynamic arrays, the size can be changed during runtime. They can grow or shrink as needed.
# Arrays can store elements of the same data type, such as integers, floats, or strings.
# Arrays are commonly used for storing and manipulating data in various applications, such as sorting, searching, and mathematical computations.

# Example of a static array in Python using the array module:
import array
# Create a static array of integers
static_array = array.array('i', [1, 2, 3, 4, 5])
print(static_array)  # Output: array('i', [1, 2, 3, 4, 5])
# Example of a dynamic array in Python using a list:
# Create a dynamic array (list) of integers
dynamic_array = [1, 2, 3, 4, 5]
print(dynamic_array)  # Output: [1, 2, 3, 4, 5]
# In Python, lists are dynamic arrays that can grow and shrink as needed. You can add or remove elements from a list using various methods, such as append(), insert(), remove(), and pop().

