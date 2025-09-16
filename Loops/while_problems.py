# 1.Count digits of a number

num = 98765
count = 0
while num > 0:         # loop runs until num becomes 0
    num //= 10         # remove last digit
    count += 1         # increase count
print("Number of digits =", count)

# Output: Number of digits = 5

# Explanation:
# num = 98765 → count = 0
# num = 9876 → count = 1
# num = 987 → count = 2
# num = 98 → count = 3
# num = 9 → count = 4
# num = 0 → count = 5 → loop ends.


# 2.Sum of digits of a number

num = 1234
total = 0

while num > 0:
    digit = num % 10       # get last digit
    total += digit         # add to total
    num //= 10             # remove last digit
print("Sum of digits =", total)

# output: Sum of digits = 10

# Explanation: 
# num = 1234 → digit = 4 → total = 4
# num = 123 → digit = 3 → total = 7
# num = 12 → digit = 2 → total = 9
# num = 1 → digit = 1 → total = 10
# num = 0 → loop ends.



# 3.Reverse a number

num = 1234
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number =", reverse)

# output: Reversed number = 4321

# Explanaton: 
# num = 1234 → digit = 4 → reverse = 0*10+4 = 4
# num = 123 → digit = 3 → reverse = 4*10+3 = 43
# num = 12 → digit = 2 → reverse = 43*10+2 = 432
# num = 1 → digit = 1 → reverse = 432*10+1 = 4321
# num = 0 → loop ends.


# 4.Sum of even and odd numbers up to n

n = 10
i = 1
even_sum = 0
odd_sum = 0

while i <= n:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    i += 1

print("Sum of even numbers =", even_sum)
print("Sum of odd numbers =", odd_sum)

# output: Sum of even numbers = 30
#         Sum of odd numbers = 25





