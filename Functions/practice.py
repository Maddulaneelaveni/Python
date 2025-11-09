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



# 3. Find the Largest of Three Numbers

def largest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(largest(10, 25, 15))  # Output: 25



# 4. Calculate Factorial of a Number

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)   # using recursion
    
print(factorial(8))  # Output: 40320



# 5.Return Sum of a List

def sum_list(numbers):
    return sum(numbers)  # using built-in sum function
print(sum_list([2,4,6,8]))  # Output: 20



# 6.Count Vowels in a String

# Loops thrpugh each character and checks if it's a vowel.
def count_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for ch in s:
        if ch in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))  # Output: 3



# 7.Find Maximum of Two Numbers

def max_two(a,b):
    if a>b:
        return a
    else:
        return b
print(max_two(10,25)) # Output: 25



# 8.Check if number is prime

def is_prime(num):
    if num <=1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(is_prime(11))  # Output: True



# 9.Word Capitalizer