# What is a string in Python?
# A string is just text – a sequence of characters.
name = "Neelaveni"
city = 'Hyderabad'
greeting = "Hello, how are you?"
multiline_string = """This is a string that spans multiple lines using triple quotes."""

# String Operations
# Concatenation
full_greeting = greeting + " My name is " + name + " and I live in " + city + "."
print(full_greeting)

# Repetition
echo = "Hello! " * 3
print(echo)

# Accessing Characters
first_letter = name[0]  # 'N'
last_letter = name[-1]  # 'i'
print("First letter:", first_letter)
print("Last letter:", last_letter)


# Slicing
substring = name[1:5]  # 'eelav'
print("Substring from index 1 to 4:", substring)


# String Methods
upper_case = name.upper()
print("Uppercase:", upper_case)

lower_case = city.lower()
print("Lowercase:", lower_case)

length = len(greeting)
print("Length of greeting:", length)

replaced_string = greeting.replace("Hello", "Hi")
print("Replaced string:", replaced_string)


# Finding Substrings
index_of_hyphen = greeting.find("how")
print("Index of 'how':", index_of_hyphen)   

# Splitting Strings
words = greeting.split(" ")
print("Words in greeting:", words)

# Joining Strings
joined_string = "-".join(words)
print("Joined string with hyphens:", joined_string)

# Stripping Whitespace
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()
print("Stripped string:", stripped_string)

# Formatting Strings
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)
f_string = f"My name is {name} and I am {age} years old."
print(f_string)

# Escape Characters
escaped_string = "He said, \"Hello!\"\nWelcome to Python programming."
print(escaped_string)

# Raw Strings
raw_string = r"C:\Users\Neelaveni\Documents"
print("Raw string:", raw_string)

# String Membership
is_in_name = 'N' in name
print("Is 'N' in name?", is_in_name)
is_not_in_city = 'z' not in city
print("Is 'z' not in city?", is_not_in_city)


# String Comparison
string1 = "apple"
string2 = "banana"
are_equal = string1 == string2
print("Are the two strings equal?", are_equal)
is_greater = string1 > string2
print("Is 'apple' greater than 'banana'?", is_greater)  
is_less = string1 < string2
print("Is 'apple' less than 'banana'?", is_less)    
is_not_equal = string1 != string2
print("Are the two strings not equal?", is_not_equal)

# String Immutability
original_string = "Hello"
modified_string = original_string.replace("H", "J")
print("Original string:", original_string)
print("Modified string:", modified_string)
# Note: Strings in Python are immutable, meaning they cannot be changed after they are created.


# Slicing strings
# Slicing = taking a part (substring) of the string.

# Syntax:
# string[start:end:step]

# start → index where slice begins (inclusive)

# end → index where slice stops (exclusive)

# step → jump size (optional)


