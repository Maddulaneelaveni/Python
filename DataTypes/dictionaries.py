# 1. Dictionary type
d = {"name": "Neelu", "age": 22, "city": "Hyderabad"}
print(type(d))  

# 2. Access value
print(d["name"])   # prints Neelu

# 3. Add key-value
d["country"] = "India"
print(d)   #prints {'name': 'Neelu', 'age': 22, 'city': 'Hyderabad', 'country': 'India'}

# 4. Update value
d["age"] = 23
print(d)   # prints {'name': 'Neelu', 'age': 23, 'city': 'Hyderabad', 'country': 'India'}

