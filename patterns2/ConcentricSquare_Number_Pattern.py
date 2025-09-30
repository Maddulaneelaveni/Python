# Concentric square Number Pattern

# A concentric square number pattern is a square of numbers arranged in layers.
# The outermost layer has the highest number (equal to n)
# Each inner layer decreases the number byn1, until the center is 1.
# the pattern is symmetric both horizontally and vertically

# How to solve it:

# The size of the square = 2*n-1
# for example: if n=4. then the size=7 rows*7 columns.

# for each position (i,j) in the square:

# Calculate the minimum distance from the 4 edges:
# Distance from the top edge=i
# Distance from left edge = j
# Distance from the bottom edge=size-1-i
# Distance from the right edge=size-1-j

# The smallest of these values = how deep we are inside the square
# Subtract that depth from n. so that it gives the number to print.

# Formula = n-min(i,j,size-1-i,size-1-j)


# Concentric Square Number Pattern

n=4   # number at the outermost layer.
size=2 * n - 1     # Total rows and columns. For n=4, size=7.
for i in range(size):  # Loop through each row (0 to size-1)
    for j in range(size):  # Loop through each column (0 to size-1)
        min_dist=min(i, j, size - 1 - i, size - 1 - j)
        # Subtract the distance from n to know which layer number to print
        # Outermost layer = n, next inner layer = n-1, ..., center = 1
        print(n-min_dist,end=" ")
    print()  # After finishing one row, go to the next line
