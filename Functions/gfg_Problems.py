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

