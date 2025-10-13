# 1.For loop:

# The for loop is used to iterate over a sequence (like a list, tuple, string, or range of numbers).
# Syntax:
#for variable in sequence:
    # code to execute

# Example:Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# 2.Using range()
for i in range(5):  # 0 to 4
    print(i)



# 2. WHILE LOOP:
#The while loop runs as long as a condition is True.

# Syntax:
# while condition:
    # code to execute

# example:
# Simple while loop
i = 1
while i <= 5:
    print(i)
    i += 1


# Using while with break
i = 1
while True:
    print(i)
    if i == 3:
        break
    i += 1


# 3. Control Statements in Loops:

# break – exits the loop completely.

# continue – skips the current iteration and moves to the next.

# else with loops – executes a block of code if the loop completes normally (no break).


# 4. Nested Loops:
# You can have a loop inside another loop.

# Example:
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

