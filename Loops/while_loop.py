# While loop:

# A while loop is used to repeatedly execute a block of code as long as a condition is true.

# syntax:
# while condition:
    # code to execute

# condition → a logical expression (evaluates to True or False).

# The loop runs until the condition becomes False.

# If the condition is never False, the loop runs infinitely.

# Example:Simple Counter(Print numbers from 1 to 5)
i = 1
while i <= 5:
    print(i)
    i += 1

# output:
# 1
# 2
# 3
# 4
# 5

# Explanation:

# Starts with i = 1

# Prints until i <= 5

# i += 1 increases i each time

# When i = 6, condition becomes False, loop ends.


# 2.Print even numbers from 2 to 10

i = 2                 # start with first even number 2
while i <= 10:        # run loop until i becomes greater than 10
    print(i)          # print the current number
    i += 2            # increase i by 2 (to get next even number)

# output:
2
4
6
8
10


# 3.Print squares of numbers from 1 to 5

i=1
while i <= 5:
    print(i*i)
    i += 1

# Output:
1
4
9
16
25


# 4.Print a countdown from 5 to 1

i = 5
while i > 0:
    print(i)
    i -= 1

# output:
5
4
3
2
1


# 5.Print "Hello" 3 times

i = 1
while i <= 3:
    print("Hello")
    i += 1

# output:
# Hello
# Hello
# Hello



