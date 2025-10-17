# Continuous Incrementing Number Triangle (Floyd’s Triangle)

n=5   # total number of rows
num = 1    # starting number
for i in range(1, n + 1): # Outer loop: for each row (1 to n)
    for j in range(1, i + 1): # Inner loop : controls how many numbers to print in that row
        print(num, end=" ")  # print current number on the same line
        num += 1    # increment number for next print
    print()   
# output:
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15
