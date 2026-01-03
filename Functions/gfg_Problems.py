# 1. Check Even or Odd
def Even_Or_Odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: ")) # Taking the input from user
result = Even_Or_Odd(num) # calling the function
print("The number is", result)

# 2. Multiplication Table
def multiplication_table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num * i}")
num = int(input("Enter a number"))
multiplication_table(num) # calling the function

# 3.Sum of Naturals
def sum_of_naturals(n):
    return n * (n+1) // 2
n = int(input("Enter a natural number: "))
print("Sum of natural numbers is:", sum_of_naturals(n))

# 4.Sum of squares of naturals
def sum_of_naturals(n):
    return n * (n+1) * (2*n + 1) // 6
n = int (input("Enter a natural number: "))
print("Sum of sqaures of natural numbers is:", sum_of_naturals(n))

# 5. Swap Two Numbers
# Swap using Temporary variable
def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b
x= int(input("Enter the first number: "))
y = int(input("Enter second number: "))
# calling the function
x,y = swap_numbers(x,y)
print("After swapping:")
print("x=", x)
print("y =", y)

# Swap without using temporary variable
def swap_numbers(a, b):
    a, b = b, a
    return a, b
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
x , y=swap_numbers(x,y)
print("x=", x)
print("y=", y)

# 6.Closest number
def closest_integer(num):
    return round(num)  
# Taking input from user
num = float(input("Enter a number: "))
# Calling the function
result = closest_integer(num)
print("Closest integer is:", result)

# 7. Dice problem
# Dice Roll
import random
def roll_dice():
    return random.randint(1, 6)
# calling the funtion
result=roll_dice()
print("Dice rolled:", result)

#8. Check if dice roll is EVEN or ODD
import random
def even_or_odd_dice():
    roll = random.randint(1, 6)
    if roll % 2 == 0:
        print(roll, "is Even")
    else:
        print(roll, "is Odd")
even_or_odd_dice()

# 9.Nth term of AP
def nth_term_ap(a, d, n):
    return a + (n - 1) * d
a = int(input("Enter first term: "))
d = int(input("Enter common difference: "))
n = int(input("Enter term number: "))
print("Nth term of AP is:", nth_term_ap(a, d, n))

#                    (OR)

def nth_term_ap(a, d, n):
    return a+(n - 1)*d
# Example
a = 2 # first term
d = 3   # common difference
n = 5  # term number
print("Nth term of AP is:", nth_term_ap(a, d, n))

# 9. check the type of traingle
def is_valid_triangle(a, b, c):
    return a + b + c == 180 and a > 0 and b > 0 and c > 0
a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))
if is_valid_triangle(a, b, c):
    print("Valid Triangle")
else:
    print("Not a Valid Triangle")

# 10.Find angle c of a triangle and check validity [a,b are given]
def find_angle_c_and_check_validity(a, b):
    c=180-(a+b)
    if a>0 and b>0 and c>0:
        print("Angle c is:", c)
        print("Valid Triangle")
    else:
        print("Not a Valid Triangle")
a = int(input("Enter angle a: "))
b = int(input("Enter angle b: "))
find_angle_c_and_check_validity(a, b) 

# Logic and output are mixed together
# Function cannot be reused or tested easily 
# How it works :
# Function calculates c
# Function prints result itself
# No value is returned

#                    (OR)
def find_angle_c_and_check_validity(a, b):
    c = 180 - (a + b)
    if a > 0 and b > 0 and c > 0:
        return c, True
    else:
        return c, False
a = int(input("Enter angle a: "))
b = int(input("Enter angle b: "))
c, is_valid = find_angle_c_and_check_validity(a, b)
if is_valid:
    print("Angle c is:", c)
    print("Valid Triangle")
else:
    print("Not a Valid Triangle")

# This approach separates LOGIC (function) and OUTPUT (main code)
# How it works :
# Function calculates c
# Function returns two values:
# c (calculated angle)
# True / False (validity)
# Outside the function:
# Values are stored in variables
# Printing decision is made

# 11. Sum of digits of a number
def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10   # get last digit
        total += digit  # add to sum
        n //= 10   # remove last digit
    return total
num = int(input("Enter a number: "))
print("Sum of digits is:", sum_of_digits(num))

# 12. Difference between two points
import math
def distance(p1, p2):   # USing tuples to represent points and math.dist() to calculate distance
    return math.dist(p1, p2)
print(distance((1, 2), (4, 6)))  

# 13. Reverse Digits of a number
def reverse_digits(n): # n is the input number
    rev = 0 # rev stores the reversed number and starts initially 0
    while n > 0: # loop until n becomes 0, and when n becomes 0, all digits are reversed
        digit = n % 10  # get the last digit of number n
        rev = rev * 10 + digit # rev*10 shifts digits left (rev) and adds new digit at the end
        n //= 10 # removes the last digit from n
    return rev





