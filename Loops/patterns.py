# 1. print the following pattern(numbers):
1 
12 
123 
        
1234

# Number pattern

n=4   # number of rows
for i in range(1,n + 1):        # loop for rows
    for j in range(1, i + 1):    # loop for numbers in each row
        print(j, end="")         # print numbers in same line without space
    print()                      # move to the next line



# 2.   Print a pyramid pattern: 
# * 
# ** 
# *** 
# **** 
# ***** 

n=5   # number of rows

for i in range(1,n + 1):       # loop for rows
    for j in range(i):          # print i stars in each row
        print("*", end="")
    print()                     # move to next line





n=5   # number of rows
for i in range(n,0,-1):       # loop from 5 down to 1
    for j in range(i):          # print i stars in each row
        print("*", end="")
    print()                     # move to next line

