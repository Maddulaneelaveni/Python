# Conditional Statements are decision-making statements in programming.
# They allow the program to execute certain blocks of code only if a specific condition is true.

# Types of Conditional Statements in Python:

# 1.if statement :
# Executes a block of code only if the condition is true.

# Example:
age = 20
if age >= 18:
    print("You are eligible to vote.")


# 2.if-else statement:
# Executes one block if the condition is true, otherwise another block.

# Example:
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")



# 3.if-elif-else ladder
# Used when you have multiple conditions to check.

# example:
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")



# 4.Nested if statements
# An if inside another if.

# Example:
number = 25
if number > 0:
    if number % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
