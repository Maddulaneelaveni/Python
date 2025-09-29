# Palindromic Number Triangle pattern

n = 5      # number of rows
for i in range(1, n + 1):  
    # Left half: numbers from 1 up to i 
    for j in range(1, i + 1): # j iterates 1,2,...,i
        print(j, end="")    # print the number without newline; end="" keeps characters adjacent
    # Right half: numbers from (i-1) down to 1 to complete the palindrome
    for j in range(i - 1, 0, -1):  # j iterates i-1, i-2, ..., 1
        print(j, end="")     # print adjacent to left half (no spaces)
    print()   # finish the row and move to the next line 

# Output (n=5):
# 1
# 121
# 12321
# 1234321
# 123454321
