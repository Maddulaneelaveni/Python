# 1.Panlindrome
# A number is a palindrome if it reads the same forward and backward.

num=int(input("Enter a number: "))
temp=num   # store original value
rev=0      # variable to store reverse
while num>0:
    digit=num%10      # Extract last digit
    rev=rev*10+digit  # build reverse number
    num=num//10    # removes last digit
if temp==rev:
    print("Palindrome")
else:
    print("Not palindrome")