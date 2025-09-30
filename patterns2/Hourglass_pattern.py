# Hourglass stars pattern

n=5     # total no.of rows
# Top (inverted pyramid)
for i in range(n, 0, -1):  # iterate from n down to 1
    spaces = n-i   # leading spaces to align center
    stars = 2*i-1    # decreasing star count
    print(" " * spaces + "*" * stars)  # print inverted pyramid row

# Bottom (normal pyramid) 
for i in range(2, n + 1):
    spaces = n-i
    stars = 2*i-1
    print(" " * spaces + "*" * stars)

# Output :

# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********



# Hourglass Hollow Pattern

n=5  # Size
# Top half of the hourglass (inverted triangle).
for i in range(n, 0, -1):  # Loop from n down to 1.
    for j in range(1, n*2):    # For each row, loop through positions from 1 to 2*n-1.
        if j==n-i+1 or j==n+i-1 or i==n:  # Condition: left edge, right edge, or top boundary.
            print("*", end="")
        else:
            print(" ", end="")  # Print spaces for hollow part.
    print()   # Move to next line.

# Bottom half of the hourglass (normal triangle).
for i in range(2, n+1):                     # Loop from 2 to n.
    for j in range(1, n*2):
        if j==n-i+1 or j==n+i-1 or i==n:  # Condition for edges and bottom row.
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Output :

# *********
#  *     *
#   *   *
#    * *
#     *
#    * *
#   *   *
#  *     *
# *********

