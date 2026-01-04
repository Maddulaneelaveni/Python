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
person = ("Neelaveniata Analyst")
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


