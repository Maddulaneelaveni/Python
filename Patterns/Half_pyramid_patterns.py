# 1.Half pyramid pattern using Loop

rows=5
for i in range(1,rows+1):   # loop from 1 to rows
    print("*" * i)



# 2.Inverted Half pyramid

rows=5
for i in range(rows,0,-1):    # loop from rows down to 1
    print("*"*i)



# 3.Pyramid patterns with numbers

rows=5
for i in range(1,rows+1):     # loop from rows to 1
    for j in range(1,i+1):    # loop from 1 to current row number
        print(j,end=" ")      # print numbers in increasing order
    print()   #move to next line



# 4.Half pyramid with alphabets

rows=5
alphabet=65  # ASCII value of "A"
for i in range(1,rows+1):    # loop through rows
    for j in range(i):       # prints i alphabets
        print(chr(alphabet+j),end=" ")   # convert ASCII to char
    print()

