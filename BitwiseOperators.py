# Bitwise Operators are used to perform operations on binary(bit-level)
# Include and(&), xor(^), not(~), left shift(<<), right shift(>>)
# Used in file permissions, compression, networking

# Problems

# 1.Input two integers and print their &, |, and ^
# Input two integers
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("a & b =", a & b)   # Bitwise AND
print("a | b =", a | b)   # Bitwise OR
print("a ^ b =", a ^ b)   # Bitwise XOR


# 2.Input an integer and print its left shift by 2 and right shift by 2
num = int(input("Enter an integer: "))
print("Left Shift by 2:", num << 2)   # multiply by 2^2 = 4
print("Right Shift by 2:", num >> 2)  # divide by 2^2 = 4


# 3.Input a number and check if it is odd or even using num & 1

num = int(input("Enter a number: "))

if num & 1:   # if last bit is 1 → odd
    print(num, "is Odd")
else:
    print(num, "is Even")




