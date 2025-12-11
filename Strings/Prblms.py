# Basic string operations:

# a) Concatenation (joining)
first = "Gram"
second = "Ujjwala"
result = first + " " + second   # "Gram Ujjwala"


# b) Repetition
s = "Ha"
print(s * 3)   # "HaHaHa"

# c) Accessing characters
word = "Python"
first_char = word[0]   # 'P'
last_char = word[-1]   # 'n'
print("First character:", first_char)
print("Last character:", last_char)

# d) Slicing
substring = word[1:4]   # 'yth'
print("Substring from index 1 to 3:", substring)

# Change case
s = "Hello World"

print(s.lower())    # 'hello world'
print(s.upper())    # 'HELLO WORLD'
print(s.title())    # 'Hello World'
print(s.capitalize())  # 'Hello world'
print(s.swapcase()) # 'hELLO wORLD'
print(s.casefold()) # 'hello world'

# Trim whitespace
s = "   Hello World   "
print(s.strip())    # 'Hello World'
print(s.lstrip())   # 'Hello World   '
print(s.rstrip())   # '   Hello World'
print(s.replace(" ", ""))  # 'HelloWorld'


# Split and Join
s = "Hello,World,Python"
parts = s.split(",")   # ['Hello', 'World', 'Python']
print("Split parts:", parts)
joined = "-".join(parts)  # 'Hello-World-Python'
print("Joined string:", joined)




