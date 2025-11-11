# List provides many built in methods for easy manipulation.

# List Methods:

numbers=[10, 20, 30, 40]

numbers.append(50) # Add item at the end
print(numbers)  # [10, 20, 30, 40, 50]

numbers.insert(2, 25)  # Insert at index 2
print(numbers) # [10, 20, 25, 30, 40, 50]

numbers.remove(25)  # Remove value
print(numbers)  # [10, 20, 30, 40, 50]

numbers.pop() # Remove last element
print(numbers) # [10, 20, 30, 40]

numbers.reverse()   # Reverse list
print(numbers)  # [40, 30, 20, 10]

numbers.sort()   # Sort ascending
print(numbers) # [10, 20, 30, 40]

print(len(numbers)) # Length → 4

count=numbers.count(20)  # count occurences

index=numbers.index(30)  # find index of value


#  Adding Elements:

fruits=["apple", "banana"]

fruits.append("cherry")  # Add at end
print(fruits)  # ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")  # Insert at index 1
print(fruits)  # ['apple', 'orange', 'banana', 'cherry']

fruits.extend(["grape", "melon"])  # Add multiple elements
print(fruits)  # ['apple', 'orange', 'banana', 'cherry', 'grape', 'melon']


# Removing Elements:

fruits=["apple", "banana", "cherry", "banana"]

fruits.remove("banana")   # Removes first occurrence
print(fruits)  # ['apple', 'cherry', 'banana']

popped = fruits.pop()   # Removes last element
print(popped) # banana
print(fruits)   # ['apple', 'cherry']

del fruits[0] # Delete element by index
print(fruits)   # ['cherry']

fruits.clear()  # Empty the list
print(fruits) # []


# List comprehension:

# Normal method
squares=[]
for i in range(1, 6):
    squares.append(i*i)

# List comprehension
squares=[i*i for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# With condition
even=[x for x in range(10) if x % 2 == 0]
print(even)  # [0, 2, 4, 6, 8]


# Nested Lists (2D Lists)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])  
print(matrix[1][2])  # 6 (2nd row, 3rd column)
