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

# Check substring
s = "Hello World"
print("World" in s)    # True
print("world" in s)    # False (case-sensitive)
print(s.startswith("Hello"))  # True
print(s.endswith("Python"))   # False
print(s.count("o"))    # 2
print(s.find("lo"))    # 3
print(s.index("lo"))   # 3
print(s.rfind("o"))   # 7
print(s.rindex("o"))  # 7
print(s.isalpha())    # False (contains space)
print(s.isdigit())    # False
print(s.isalnum())    # False (contains space)
print(s.isspace())    # False
print(s.islower())    # False
print(s.isupper())    # False
print(s.istitle())    # True
print(s.isprintable()) # True
print(s.zfill(20))    # '0000000000Hello World'
print(s.center(30, '*'))  # '**********Hello World**********'
print(s.ljust(30, '-'))   # 'Hello World--------------------'
print(s.rjust(30, '-'))   # '--------------------Hello World'
print(s.partition(" "))  # ('Hello', ' ', 'World')
print(s.rpartition(" ")) # ('Hello', ' ', 'World')
print(s.splitlines())   # ['Hello World']
print(s.encode())      # b'Hello World'





