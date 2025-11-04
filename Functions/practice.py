# 1. Find Square of a Number
def square(num):
    return num * num
print(square(4))  # Output: 16


# 2. Check if a Number is Even or Odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(9))  # Output: Odd