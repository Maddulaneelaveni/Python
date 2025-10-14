# Tuples:
# A tuple is a collection of ordered, immutable elements in Python.

# syntax:
my_tuple = (1, 2, 3)

# Key charactersistics:
# ordered, immutable, allows duplicates, can store diffrenr data types

# Ex:
info=("Neelaveni", 20, 5.4, True) # A tuple can have different types
print(info)

# Creating Tuples
t1=(10, 20, 30)

# Single-element tuple:
# You must use a comma after the element:
t3=(10,)   # Valid
t4=(10) #  Not a tuple, it's an int

# Nested tuple:
nested=(1, (2, 3), (4, 5))


# Accessing Tuple Elements:

# 1. By index:

t=(10, 20, 30, 40)
print(t[0]) # 10
print(t[-1]) # 40

# 2.Slicing:

print(t[1:3]) # (20, 30)
print(t[:3]) # (10, 20, 30)


# Tuple Operations:
# 1. concatenation - "+", ex:(1,2)+(3,4) → (1,2,3,4)
# 2. Repitition - "*", ex:(1,2)*2 → (1,2,1,2)
# 3. Membership - in , ex:2 in (1,2,3) → True
# 4. Length - len() , ex: len((1,2,3)) → 3
# 5. Highest/lowest - max(),min() , ex:max((5,10,2)) → 10
# 6. sum of numbers - sum() , ex:sum((1,2,3)) → 6


#  Nested Tuples Access:
t = (1, (2, 3, (4, 5)))
print(t[1][2][1])  # Accessing 5


# Tuple Methods:
# Tuples have only two built-in methods:

# 1. ".count(value)" - counts occurences - ex:1,2,1,3).count(1) → 2
# 2. ".index(value)" - Returns index  - ex: (10,20,30).index(20) → 1


# Sorting a Tuple:
# Tuples are immutable, but can sort using sorted():
t = (5, 1, 3)
print(sorted(t))  # [1, 3, 5]




