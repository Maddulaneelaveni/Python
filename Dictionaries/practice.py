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



# 3.Find the Key with the Maximum Value
# Find which student scored the highest.

scores = {"Neelu": 88, "Mokshi": 92, "Vinya": 85, "Manu": 95}
top_student = max(scores, key=scores.get)  # # Use max() with key parameter
print("Top student:", top_student)



# 4.Convert Two Lists into a Dictionary

names = ["Neelu", "Mokshi", "Vinni"]
marks = [85, 90, 88]
result = dict(zip(names, marks)) # Use zip() to pair items and dict() to convert
print(result)



# 5.Access Value 

customer = {"name": "Neelaveni", "email": "neelaveni@example.com"}
print("Name:", customer.get("name"))
# .get() return value if key exists, if not it returns the default message instead of error.



# 6.Word Frequency Counter (count how many times each word appears.)

sentence = "Hello python, python is easy"
words = sentence.split() # Split sentence into individual words
word_count = {} # Create an empty dictionary for word count
for word in words: #Loop through each word and count frequency
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)



# Merge Sales Data:
# two months’ sales data and need a combined total.

jan_sales = {"apple": 40, "banana": 50}
feb_sales = {"banana": 30, "cherry": 25}
combined = {} # Create an empty dictionary for combined data
# Combine both using set union of keys
for item in set(jan_sales) | set(feb_sales):
    combined[item] = jan_sales.get(item, 0) + feb_sales.get(item, 0)
print(combined)



# Sort Employee Salaries
# employee names with salaries and want to show them sorted by salary.

salaries = {"Mokshi": 45000, "Vinya": 55000, "Neelu": 40000}
# Sort dictionary by value (salary)
sorted_salaries = dict(sorted(salaries.items(), key=lambda x: x[1]))
print(sorted_salaries)

# salaries.items() → returns key-value pairs.
# lambda x: x[1] → sorts by salary (value).
# dict(sorted(...)) → converts result back to a dictionary.
