# 1.Create and Access Dictionary Elements

student = {"name": "Neelaveni", "age": 22, "course": "Data Science"}

# Accessing elements using keys
print("Name:", student["name"])     # prints the value of 'name'
print("Age:", student["age"])       # prints the value of 'age'


# 2.Count Frequency of Each Character in a String
word = "apple"
freq = {}  # Empty dictionary to store frequency
for char in word:
    freq[char] = freq.get(char, 0) + 1  # get() returns 0 if char not found, then add 1
print(freq)
