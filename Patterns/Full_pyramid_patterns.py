# 1. Full Pyramid Pattern
rows=5  # no.of rows
for i in range(rows):    # this loop iterates each row from 0 to 4
    # Print spaces
    for j in range(rows- i-1):  # prints the necessary spaces before the asterisks
        print(" ", end="")    # Prints a single space without a new line.
    # Print asterisks
    for k in range(2*i+1):  # prints the number of asterisks for the current row.
        print("*", end="")
    print()

# output:
#    A
#   BBB
#  CCCCC
# DDDDDDD
#EEEEEEEEE


# 2.Pyramid with Alphabets

# prints a pyramid using letters of the alphabet. It uses the chr() function to convert an ASCII value to a character. The pattern repeats letters within each row.

rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print(chr(65 + i), end="")    # ascii value A=65, `chr()` converts the ASCII value `65 + i` to a character. For `i=0`, it's 'A', for `i=1` it's 'B', and so on.
    print()
# output:
#    A
#   BBB
#  CCCCC
# DDDDDDD
#EEEEEEEEE



# 3.Pyramid with Numbers
# pyramid where each row contains the same number, corresponding to the row number.

rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print(i + 1, end="")
    print()

# output:
  # 1
  #222
 #33333
#4444444
#555555555




