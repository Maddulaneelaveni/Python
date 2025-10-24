# Dictionary
# A dictionary in Python is a collection of key–value pairs.
# It allows you to store data that can be accessed using a unique key instead of an index (like in lists or tuples).

#syntax:
my_dict = {key1: value1, key2: value2, key3: value3}

# Characteristics:
# 1.Unordered
# 2.Mutable
# 3.Indexed by keys
# 4.No duplicate keys


# Creating Dictionaries:

# 1.Using {} braces:
student = {"name": "Neelaveni", "age": 22, "course": "Data Science"}

# 2.Using the dict() constructor:
student = dict(name="Neelaveni", age=22, course="Data Science")

# 3.Creating an empty dictionary:
student = {}


# Accessing Dictionary Items:

# 1. Using keys:
print(student["name"])   

# 2. Using .get() method :
print(student.get("age"))        
print(student.get("grade", "N/A"))  



# Adding and Updating Items:

# Add new key-value pair:
student["grade"] = "A"

# Update existing key:
student["age"] = 23

# Update multiple at once:
student.update({"course": "AI", "city": "Hyderabad"})


# Removing Items;

# 1. pop(key)
# 2.del
# 3.popitem()
# 4.clear()





