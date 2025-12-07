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


