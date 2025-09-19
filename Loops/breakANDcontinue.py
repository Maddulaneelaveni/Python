# 1.break statement:
# Used to terminate (exit) the loop completely.
# Once break is executed, the loop stops immediately, and control moves to the code after the loop

#example:
for i in range(1, 10):
    if i == 5:
        break   # loop will stop when i = 5
    print(i)

print("Loop ended")

# output: 1
# 2
# 3
# 4
# Loop ended


# 2. continue statement:
# Used to skip the current iteration and move to the next one.
# It does not terminate the loop.

# example:
for i in range(1, 10):
    if i == 5:
        continue   # skip printing when i = 5
    print(i)

print("Loop finished")

# output:
1
2
3
4
6
7
8
9
Loop finished


# 3. Using break and continue in a while loop

i = 0
while i < 10:
    i += 1
    if i == 3:
        continue   # skip printing 3
    if i == 7:
        break      # stop when i = 7
    print(i)

#output:
# 1
# 2
# 4
# 5
# 6


# break → exits the loop completely.

# continue → skips the current iteration and continues with the next one.

