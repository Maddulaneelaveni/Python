# Floyd's Triangle pattern
# output:
#1
#2 3
#4 5 6
#7 8 9 10

n = 4   # no.of rows
num = 1  # starting number
for i in range(1, n+1):  # loop through rows
    for j in range(i):   # loop through columns in each row
        print(num, end=" ")  # print current number
        num += 1    # move to next number
    print()    # new line after each row



#   Reverse Floyd’s Triangle

# output:
#10 9 8 7
#6 5 4
#3 2
#1


n = 4        # number of rows
num = n * (n + 1) // 2   # start from the last number in the triangle

for i in range(n, 0, -1): # loop rows in reverse
    for j in range(i):   # print i numbers in that row
        print(num, end=" ") # print current number
        num -= 1   # decrease number
    print()      # move to next line


