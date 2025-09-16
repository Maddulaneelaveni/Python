# 1. print pattern in reverse

for i in range(5, 0, -1):
    print("*" * i)

# Output:
# *****
# ****
# ***
# **
# *


# 2.Fibonacci sequence up to n terms

# Fibonacci sequence starts with 0, 1.

# Each new number = sum of the previous two.

# Variables a and b keep track of the last two numbers.

# After printing a, we update:

# a = b

# b = a + b (old a + b)

n=10
a,b=0,1
for _ in range(n):
    print(a, end=" ")
    a,b=b, a+b

# output:
# 0 1 1 2 3 5 8 13 21 34



# 3.Pyramid pattern (spaces+odd stars)

# We want a pyramid with 5 rows.

# For each row i:

# Spaces = (rows - i - 1) → makes stars shift to the center.

# Stars = (2*i + 1) → increases odd numbers: 1, 3, 5, 7, 9.

rows = 5
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2*i + 1))

# output:
 #   *
 #  ***
 # *****
 #*******
#*********


# 4. Largest number in a list (without max())

nums = [10, 25, 3, 99, 56]
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print("Largest number =", largest)

# output:
# Largest number = 99

# Explanation:
# Start by assuming the first number is the largest (largest = nums[0]).

# Loop through each number n in the list.

# If any number is greater than the current largest, update it.

# After the loop, largest holds the biggest number → 99.



