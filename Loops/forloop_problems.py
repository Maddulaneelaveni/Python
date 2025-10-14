# For loop problems:

# 1.Print numbers from 1 to 10

for i in range(1, 11):
    print(i)


# 2.Print all characters of "Python"

for char in "Python":
    print(char)


# 3.Sum of numbers from 1 to 100

total = 0
for i in range(1, 101):
    total += i
print("Sum =", total)


# 4.Even numbers between 1 and 20

for i in range(2, 21, 2):
    print(i)


# 5.Factorial of a number

num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial of", num, "=", fact)


# 6.Prime numbers between 1 and 50

for num in range(2, 51):   # numbers from 2 to 50
    for i in range(2, num):   # check divisors from 2 to num-1
        if num % i == 0:      # if divisible, not prime
            break
    else:   # this else belongs to the for-loop (executes if loop not broken)
        print(num, end=" ")


# 7.Count vowels in a string

text = "programming is fun"
vowels = "aeiou"
count = 0
for ch in text:
    if ch.lower() in vowels:
        count += 1
print("Vowel count =", count)


# 8.Reverse a string using for loop

s = "Python"
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string =", rev)


# 9.Print pattern

for i in range(1, 6):
    print("*" * i)

# output:
# *
# **
# ***
# ****
# *****

