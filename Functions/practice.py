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

# Capitalize the first letter of every word in a sentence.
def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())
print(capitalize_words("python functions are powerful"))
# Output: Python Functions Are Powerful

# 10.Fibonacci Sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 11.Remove all spaces from a string
def remove_spaces(s):
    return s.replace(" ", "")
print(remove_spaces("Hello World"))  # Output: HelloWorld

# 12.Check if a string is palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]
print(is_palindrome("A man a plan a canal Panama"))  # Output: True

# 13.Find GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(48, 18))  # Output: 6

# 14.Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(celsius_to_fahrenheit(25))  # Output: 77.0

# 16.Check if a number is Armstrong number
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == num

# 17. Program showing Local & Global variable difference
x = 50   # Global variable
def show():
    x = 20   # Local variable
    print("Inside function:", x)
show()
print("Outside function:", x)
# output : Inside funtion:20
# Outside function:50

# write a funcrion that modifies a global variable
count = 10   # Global variable
def update():
    global count
    count = count + 5
update()
print("Updated value:", count)
# output: Updated value:15
# global keyword allows modification and use global only when modifiaction is required.



