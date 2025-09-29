# Butterfly pattern

n = 4     # wing height; the total height of butterfly will be 2*n (top + bottom)
# Top half: rows 1..n
for i in range(1, n + 1):  
    left_wing = "*" * i    # left wing: repeat '*' i times
    # middle gap width = 2*(n-i)
    middle_gap = " " * (2 * (n - i))
    right_wing = "*" * i      # right wing identical to left wing
    # Concatenate left wing, gap, and right wing to form a full line
    print(left_wing + middle_gap + right_wing)  # prints top half rows

# Bottom half: rows n..1 (mirror). Using the same logic in reverse produces symmetric pattern
for i in range(n, 0, -1):      # start at n then decrease to 1
    left_wing = "*" * i
    middle_gap = " " * (2 * (n - i))
    right_wing = "*" * i
    print(left_wing + middle_gap + right_wing)  # prints bottom half rows

# Output 

# *      *
# **    **
# ***  ***
# ********
# ********
# ***  ***
# **    **
# *      *