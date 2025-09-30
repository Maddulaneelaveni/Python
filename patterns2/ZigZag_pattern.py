# Zig Zag Pattern

# A Zig-Zag Pattern is a wave-like star pattern printed over 3 rows where stars * appear diagonally in a repeating pattern.

# Step-by-Step Logic :

# No.of rows = 3
# No.of columns = n (width of the pattern)
# Loop through each row i (1 to 3)
# Loop through each column j (1 to n)
# Place a star * if either:
# (i + j) % 4 == 0 → diagonal stars in top and bottom rows
# (i == 2) and j % 4 == 0 → stars in middle row
# Else, place a space ' '
# After finishing each row, move to the next line

# Why % 4?
# The pattern repeats every 4 columns.
# (i + j) % 4 == 0 ensures diagonal stars for rows 1 and 3.
# (i == 2) and j % 4 == 0 ensures middle row stars align with the diagonal pattern.



# Zig-Zag Pattern

n=9        # No.of columns (width of the pattern)
rows=3      # No.of rows in the zig-zag pattern
for i in range(1, rows + 1):    # Loop through each row
    for j in range(1, n + 1):    # Loop through each column
        # Condition to print stars:
        # 1. Top and bottom rows: stars on diagonals (i+j divisible by 4)
        # 2. Middle row: stars in columns divisible by 4
        if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
            print("*", end="")  # Print star without newline
        else:
            print(" ", end="")  # Print space without newline
    print() # After finishing a row, move to next line
