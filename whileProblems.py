# 1.Find the sum of numbers from 1 to N

N = int(input("Enter N: "))
i = 1
total = 0
while i <= N:
    total += i
    i += 1
print("Sum =", total)



# 2. Fibonacci sequence up to N terms

N = int(input("Enter N: "))
a, b = 0, 1
count = 0
while count < N:
    print(a, end=" ")
    a, b = b, a+b
    count += 1



# 3.Find GCD (Greatest Common Divisor) of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:   # continue until remainder is 0
    a, b = b, a % b  #update: a becomes b, b becomes remainder

print("GCD =", a)



# 4.Count even and odd digits in a number

num = int(input("Enter a number: "))
even = odd = 0

while num > 0:
    digit = num % 10   #get last digit
    if digit % 2 == 0: #check if digit is even
        even += 1  # increase even counter
    else:
        odd += 1  #increase odd counter
    num //= 10    # remove last digit (integer division by 10)

print("Even digits:", even)
print("Odd digits:", odd)



# 5.Find factorial of N

N = int(input("Enter N: "))
fact = 1
i = 1  # starting value
while i <= N:  # loop until i reaches N
    fact *= i  # multiply fact with current i
    i += 1     # increase i by 1
print("Factorial =", fact)



# 6.Print multiplication table of a number(7)

num = 7
i = 1
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i += 1
