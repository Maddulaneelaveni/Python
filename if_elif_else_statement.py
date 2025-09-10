# 1.Find the Greatest of Two Numbers

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b:
    print("First number is greater")
elif b>a:
    print("Second number is greater")
else:
    print("Both are equal")



# 2.Check Leap year

year=int(input("Enter a year: "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("Not a leap year")



# 3.Check Vowel or Consonant
ch=input("Enter a character: ").lower()
if ch in "aeiou":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an alphabet")









