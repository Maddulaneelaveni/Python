# Hollow square pattern

n = 4  # Size of the square (no.of rows and columns)
for i in range(n): # Outer loop to handle rows
    for j in range(n): # Inner loop to handle columns
        if i == 0 or i == n-1 or j == 0 or j == n-1: 
            print("*", end="")  # Print star for boundary positions
        else:
            print(" ", end="")  # Print space for inner (hollow) part
    print()  # Move to the next line after finishing each row

# Condition to check if we are at the boundary
        # i==0      -> first row
        # i==n-1    -> last row
        # j==0      -> first column
        # j==n-1    -> last column
