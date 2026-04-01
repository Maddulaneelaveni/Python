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
    





