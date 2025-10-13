# 1.Check sign and parity

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif num < 0:
    if num % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero")


# 2.Largest of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
else:
    if b > a:
        print("Largest:", b)
    else:
        print("Both are equal")



# 3.Divisibility Check

num = int(input("Enter a number: "))

if num % 2 == 0:
    if num % 3 == 0:
        print("Divisible by 2 and 3")
    else:
        print("Divisible by 2 only")
else:
    if num % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 2, 3, or 5")



# 4.Temperature Check

temp = int(input("Enter temperature in Celsius: "))

if temp >= 30:
    print("Hot")
else:
    if temp >= 20:
        print("Warm")
    else:
        print("Cold")


# 5.Positive Number Type

num = int(input("Enter a number: "))

if num > 0:
    if num < 10:
        print("Single Digit Positive")
    else:
        print("Multi-digit Positive")
else:
    print("Not a positive number")




