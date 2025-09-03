# Type conversion is of 2 types: 1.Implicit and 2. Explicit
# 1.Implicit : Python automatically converts one data type into another to avoid data loss.
# 2. Explicit: Programmer manually converts one data type into another using built-in functions like int(), float(), str(), list(), set(), dict() etc.

# Implicit Conversion problems:

# 1.Add 2 numbers (int) and (float).print 
a = 10  #int
b = 3.5   #float
c = a + b
print(c, type(c)) 

# 2.Multiply int with float
print(4 * 5.0, type(4 * 5.0))

# 3. Add True (bool) with int.
print(True + 2)   # prints the output as 3 because true -> 1

# 4. Divide 2 numbers
print(7/2, type(7/2))


# Explicit Conversion Problems:

# 5.Convert float into int
x= 10.5
print(int(x))

# 6.Convert int into str and concatenate
z = 2025
print(str(z) + " Year")

# 7. Convert list into tuple
lst = [1, 2, 3]
print(tuple(lst))

# 8.Convert "Python"(str) into list
s = "Python"
print(list(s))

# 9.Convert dict into list of keys
d = {"a": 1, "b": 2}
print(list(d.keys()))

# 10.Convert True into int
print(int(True))   # prints 1 because true is equal to 1

#11.Convert number 65 into character
print(chr(65))

# 12.Convert character 'A' into ASCII number
print(ord('A'))

# ASCII stands for American Standard Code for Information Interchange.
#It is a character encoding standard used to represent text in computers.
#Every character (letters, digits, symbols, control characters) has a numeric value (code) called its ASCII value.

