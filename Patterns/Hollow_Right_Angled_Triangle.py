# Hollow Right Angled Triangle Pattern

n = 5  # No.of rows

for i in range(1, n+1):   # Loop through rows
    for j in range(1, i+1):   # Loop through columns in row i
        if j == 1 or j == i or i == n:
            print("*", end="") # Print border stars
        else:
            print(" ", end="")  # Print spaces inside
    print()  # Next row

# output:

#*
#**
#* *
#*  *
#*****

# Explanation:

# j == 1 → first column star

# j == i → last column star

# i == n → last row all stars
