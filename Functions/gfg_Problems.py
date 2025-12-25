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

    