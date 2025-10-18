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



