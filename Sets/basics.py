# Sets:
# A set is an unordered, unindexed, and mutable collection of unique elements.

# Characteristics:
# Unordered → The elements don’t have a fixed position.
# Unique elements only → Duplicates are automatically removed.
# Mutable → You can add or remove elements.
# Can’t contain mutable types (like lists or dictionaries).

# Creating a Set:

my_set = {1, 2, 3, 4, 5}
print(my_set)


# creating empty list:
empty_set = set()   # Here, we should not use empty_set = {}
print(type(empty_set))  


# Accessing Elements in a Set:
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)



# Adding Elements:
# You can add elements using:
# add() → Adds one item
# update() → Adds multiple items

# 1. Add a single element
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)

# 2. Add multiple elements
fruits.update(["orange", "grape"])
print(fruits)


# Removing Elements:

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")  # Removes specific item, raises error if not found
fruits.discard("apple")  # Removes specific item, NO error if not found
fruits.pop()             # Removes a random element
fruits.clear()           # Removes all elements
print(fruits)


# Set Operations:
A={1, 2, 3, 4}
B={3, 4, 5, 6}

# 1.Union: | or .union():
# Combines elements from both sets (no duplicates).

# Ex:
print(A | B)
print(A.union(B))

# 2.Intersection : & or .intersection():
# Elements common to both sets.

# Ex:
print(A & B)
print(A.intersection(B))


# 3.Difference : - or .difference():
# Elements in A but not in B.

# Ex:
print(A - B)
print(A.difference(B))


# 4.Symmetric Difference – ^ or .symmetric_difference():
# Elements in either A or B, but not both.

# Ex:
print(A ^ B)
print(A.symmetric_difference(B))



# SET COMPARISON OPERATORS:

# 1. A==B  : check if sets are equal, and return a boolean value(True or False) Ex:{1,2} == {2,1} , returns True
# 2. A!=B  : Not equal -> Ex:{1,2} != {1,3}, True
# 3. A<B   : A is subset of B -> Ex: {1,2} < {1,2,3} , True
# 4. A>B   : A is superset of B -> Ex: {1,2,3} > {1,2},	True



# Set Comphrehension:
# Just like list comprehension, we can build sets concisely.

# Ex:
squares = {x**2 for x in range(6)}
print(squares)



# Frozen Set:
# A frozenset is immutable — elements cannot be added or removed.
# We can perform operations like union, intersection, etc., but cannot modify it.






