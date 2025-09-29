# Hourglass stars pattern

n = 5     # half-height; total rows will be 2*n - 1
# Top (inverted pyramid)
for i in range(n, 0, -1):  # iterate from n down to 1
    spaces = n - i   # leading spaces to align center
    stars = 2 * i - 1       # decreasing star count
    print(" " * spaces + "*" * stars)  # print inverted pyramid row

# Bottom (normal pyramid) 
for i in range(2, n + 1):
    spaces = n - i
    stars = 2 * i - 1
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
