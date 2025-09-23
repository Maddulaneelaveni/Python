# 1.Diamond pattern

n = 3   # number of rows

# upper half of diamond
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))   # print spaces then stars

# lower half of diamond
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))   # print spaces then stars

# output:
#  *
# ***
#*****
# ***
#  *
