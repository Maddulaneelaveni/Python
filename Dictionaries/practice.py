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



# 7. Merge Sales Data:
# two months’ sales data and need a combined total.

jan_sales = {"apple": 40, "banana": 50}
feb_sales = {"banana": 30, "cherry": 25}
combined = {} # Create an empty dictionary for combined data
# Combine both using set union of keys
for item in set(jan_sales) | set(feb_sales):
    combined[item] = jan_sales.get(item, 0) + feb_sales.get(item, 0)
print(combined)



# 8.Sort Employee Salaries
# employee names with salaries and want to show them sorted by salary.

salaries = {"Mokshi": 45000, "Vinya": 55000, "Neelu": 40000}
# Sort dictionary by value (salary)
sorted_salaries = dict(sorted(salaries.items(), key=lambda x: x[1]))
print(sorted_salaries)

# salaries.items() → returns key-value pairs.
# lambda x: x[1] → sorts by salary (value).
# dict(sorted(...)) → converts result back to a dictionary.



#9. Filter Products by Price Range
# You have a price list and want products below ₹1000.

products = {
    "Mouse": 500,
    "Keyboard": 1200,
    "Headphones": 800,
    "Monitor": 7000
}
affordable = {item: price for item, price in products.items() if price < 1000}   # Filter using dictionary comprehension
print(affordable)
# Dictionary comprehension filters and constructs new dictionaries 



# 10.Invert a Dictionary (Swap Keys and Values)

country_codes = {"IN": "India", "US": "United States", "JP": "Japan"}
# Swap keys ↔ values
reversed_dict = {v: k for k, v in country_codes.items()}
print(reversed_dict)



# 11.Count Customers by City
git commit --date="2025-11-15 22:00:00" -m "code updated"
customers = [
    {"name": "Mokshii", "city": "Hyderabad"},
    {"name": "vinaya", "city": "Bangalore"},
    {"name": "Neelaveni", "city": "Hyderabad"},
    {"name": "Manu", "city": "Chennai"},
    {"name": "taruni", "city": "Bangalore"}
]
city_counts = {}
for c in customers:
    city = c["city"]
    city_counts[city] = city_counts.get(city, 0) + 1
print(city_counts)
# output:
# {'Hyderabad': 2, 'Bangalore': 2, 'Chennai': 1}




# 12.Nested Dictionary – Employee Database
# You manage employee data (name, department, salary) and want to access specific details easily.

employees = {
    "E101": {"name": "Viswanath", "dept": "Data", "salary": 60000},
    "E102": {"name": "Neelaveni", "dept": "Analytics", "salary": 65000},
    "E103": {"name": "Ravi", "dept": "Development", "salary": 55000}
}
# Access Neelaveni's department
print(employees["E102"]["dept"])
# Give a raise to all employees
for emp in employees.values():
    emp["salary"] += 5000
print(employees)






