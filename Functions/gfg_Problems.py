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
print("Sum of sqaures of natural numbers is:", sum_of_sqaures(n))