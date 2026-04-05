# JSON
# JSON (JavaScript Object Notation) is a lightweight data format used to store and exchange data.

# It is:
# Human-readable
# Language-independent
# Widely used in APIs, web apps, data pipelines

# Example of JSON data:

{
  "name": "Neelaveni",
  "age": 22,
  "skills": ["Python", "SQL"],
  "is_student": false
}

# In Python, we can work with JSON using the built-in `json` module.
import json

# Convert Python object to JSON string
person = {
    "name": "Neelaveni",
    "age": 22,
    "skills": ["Python", "SQL"],
    "is_student": False
}
json_string = json.dumps(person)
print(json_string)
# Convert JSON string back to Python object
person_dict = json.loads(json_string)
print(person_dict)
# We can also read and write JSON data from files
# Writing JSON to a file
with open('person.json', 'w') as file:
    json.dump(person, file)
# Reading JSON from a file
with open('person.json', 'r') as file:
    person_from_file = json.load(file)
print(person_from_file)

# JSON is a powerful format for data interchange and is widely used in web development, APIs, and data storage.

# JSON vs Dictionaries:
# JSON is a string format, while a dictionary is a Python data structure.
# JSON keys must be strings, while dictionary keys can be of any immutable type.

# JSON	         Python
# Object	     dict
# Array	         list
# true/false	True/False
# null	         None


# Convert JSON → Python (Deserialization)
import json
data = {"name": "John", "age": 25}
json_data = json.dumps(data)
print(json_data)
print(type(json_data))

# Output :
{"name": "John", "age": 25}
<class 'str'>

# Convert Python → JSON (Serialization) :
import json
data = {"name": "John", "age": 25}
json_data = json.dumps(data)
print(json_data)
# Output :
{"name": "John", "age": 25}

# Working with Files :
# Writing JSON to a file : it is used to write JSON data to a file.
import json
data = {"name": "Neelaveni", "age": 22}
with open("data.json", "w") as f:
    json.dump(data, f)
# Output :
# A file named "data.json" will be created with the following content:
{"name": "Neelaveni", "age": 22}


# Reading JSON from a file : it is used to read JSON data from a file.
import json
with open("data.json", "r") as f:
    data = json.load(f)
print(data)
# Output :
{'name': 'Neelaveni', 'age': 22}

# 5. Pretty Printing (Formatting JSON) : it is used to format JSON data in a more readable way.
# Makes JSON readable
# Used in debugging & APIs
import json
data = {"name": "Neelaveni", "age": 22, "skills": ["Python", "SQL"]}
pretty_json = json.dumps(data, indent=4)
print(pretty_json)
# Output :
{
    "name": "Neelaveni",
    "age": 22,
    "skills": [
        "Python",
        "SQL"
    ]
}







