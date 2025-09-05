# Identity Operators are used



# problems:

# 1.Check if two lists point to same object. (is)
a = [1, 2, 3]
b = a
print(a is b)  # True


# 2.Check if two identical lists are different objects (is)
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False


# 3.Check dict references (is not)
d1 = {"a":1}
d2 = {"a":1}
print(d1 is not d2)  # True


# 4.String literals check (is)
x = "hello"
y = "hello"
print(x is y)  # True (interned)

