# 1.Count occurrences of a number
t = (1, 2, 3, 2, 4, 2, 5)
# Count how many times 2 appears
count_2 = t.count(2) # .count(value) returns how many times value appears.
print(count_2)  
# Output: 3


# 2.Access nested tuple element
nested = (1, 2, (3, 4, 5), 6)
# Access 4 from the nested tuple
print(nested[2][1])  
# Output: 4


# 3.Tuple unpacking
person = ("Neelaveni Analyst")
name, age, role = person # Unpack tuple into variables
print(name) # Neelaveni
print(age)# 21
print(role)  # Data Analyst

# 4.Tuple Membership and Conditional
t = (10, 20, 30, 40)
# Check if 25 exists
if 25 in t:
    print("Exists")
else:
    print("Does not exist")  
# Output: Does not exist

# 5.Zip Two Lists into a Tuple
names = ["Neelaveni", "Vinaya", "Mokshi"]
scores = [85, 92, 78]
# Zip them into tuple pairs
zipped = tuple(zip(names, scores))
print(zipped)
# Output: (('Neelaveni', 85), ('Vinaya', 92), ('Mokshi', 78))

# 6.Find Maximum and Minimum in Tuple
t = (5, 3, 8, 1, 4)
print("Max:", max(t))  # Max: 8
print("Min:", min(t))  # Min: 1

# 7.Convert List of Tuples to Dictionary
tuple_list = [("Neelaveni", 85), ("Vinaya", 92), ("Mokshi", 78)]
result_dict = dict(tuple_list)
print(result_dict)

# 8.Reverse a Tuple
t = (1, 2, 3, 4, 5)
reversed_t = t[::-1]
print(reversed_t)  # Output: (5, 4, 3, 2, 1)

# 9.Merge Two Tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print(merged)  # Output: (1, 2, 3, 4, 5, 6)

# 10.Find Index of an Element
t = (10, 20, 30, 40, 50)
index_30 = t.index(30) # .index(value) returns the index of the
print(index_30)  # Output: 2

# 11.Slice a Tuple
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
sliced = t[2:7:2] # From index 2 to 6, step 2
print(sliced)  # Output: (2, 4, 6)

# 12.Convert Tuple to List and Back
t = (1, 2, 3, 4, 5)
lst = list(t)  # Convert to list
lst.append(6)  # Modify list
t_modified = tuple(lst)  # Convert back to tuple
print(t_modified)  # Output: (1, 2, 3, 4, 5, 6)

# 13.Repeat Elements in a Tuple
t = (1, 2, 3)
repeated = t * 3
print(repeated)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 14.Tuple with Single Element
single_element_tuple = (42,)  # Note the comma
print(single_element_tuple)  # Output: (42,)
print(type(single_element_tuple))  # Output: <class 'tuple'>

# 15.Nested Tuple Unpacking
nested_tuple = (1, (2, 3), 4)
a, (b, c), d = nested_tuple # Unpack nested tuple
print(a)  # Output: 1   






