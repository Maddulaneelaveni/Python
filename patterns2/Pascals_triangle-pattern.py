# Pascals Triangle Pattern (Number Pattern)
n = 6  # number of rows
for i in range(n):
    # Print leading spaces
    print(" " * (n - i), end="")
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        # Formula: next = num * (i - j) // (j + 1)
        num = num * (i - j) // (j + 1)
    print()

# output:
#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
# * * * * * * 



#  Right Pascal’s Triangle
half = 4   # Controls the size of the triangle
# Top half
for i in range(1, half+1):
    print("*" * i)   # Print i stars
# Bottom half
for i in range(half-1, 0, -1):
    print("*" * i)   # Print decreasing stars
print()

# First loop prints 1 → 4 stars.
# Second loop prints 3 → 1 stars.

# output:

#*
#**
#***
#****
#***
#**
#*



# Left Pascal’s Triangle

half = 4   # Same size as before
# Top half
for i in range(1, half+1):
    print(" " * (half-i) + "*" * i)   # Spaces + stars
# Bottom half
for i in range(half-1, 0, -1):
    print(" " * (half-i) + "*" * i)   # Spaces + stars
print()

# Explanation:

# " " * (half-i) gives spaces to shift stars right.
# "*" * i gives stars.
# Top half grows from 1 → 4 stars.
# Bottom half shrinks from 3 → 1 stars.

# output:

#   *
#  **
# ***
#****
# ***
#  **
#   *



