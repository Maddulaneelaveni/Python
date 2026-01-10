# Type casting :
# Type casting is the process of converting a value from one data type to another.
# Implicit type casting:
# It is done automatically by python interpreter.
# No data loss
# Example:
a=10
b=5.5
c=a+b
print("Implicit type casting:",c)  # 15.5
print(type(c))
# Explicit type casting:
# It is done manually by the programmer using built-in functions.
# example:
x=10.5
y=int(x)
print(y)
print(type(y))

# 1.Anagram check
s1=input("Enter first string:")
s2=input("Enter second string:")
if sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("Not an Anagram")

# 2.Pattern
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end="")
    print()

# 3.Triangle validation
angle1=float(input("Enter first angle:"))
angle2=float(input("Enter second angle:"))
angle3=180-(angle1+angle2)
if angle1>0 and angle2>0 and angle3>0:
    print("Third angle is:",angle3)
    print("Valid triangle")
else:
    print("Invalid triangle")


# 4. what is dictionary in python?
# A dictionary in Python is an unordered collection of data stored in key-value pairs.
# Mutable
# Students with highest marks
# Dictionary storing student names and their marks
students={
    "A":85,
    "B":92,
    "C":78,
    "D":96,
    "E":88
}
# Finding the student with the highest marks
top_student=max(students, key=students.get)
print("Student with highest marks:",top_student)
print("Highest marks:",students[top_student])

# 5. What is string in python? check palindrome or not
# A string is sequence of characters enclosed  in single or double quotes.
# immutable
# Palindrome check
s="madam"
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# 6.Remove all spaces from a string
s="I am Neelaveni"
result=""
for ch in s:
    if ch!=" ":
        result+=ch
print(result)

# PROGRAMIZE CONTEST-PROBLEMS

# 1.Write a function to determine if a person can enter a club.
# The club only allows people who are 21 years old or older.
# Write a function that returns True if a person's age is 21 or above, otherwise returns False.
 
def can_enter_club(age):
    return age>=21
# Test the function
age=int(input("Enter your age:"))
if can_enter_club(age):
    print("Allowed to enter the club")
else:
    print("Not allowed to enter the club")

# Is pass or fail
# Write a function to check whether a student passed or failed an exam.
# Assume the pass marks to be 50
# Return passed if the student scored more than 50. otherwise return failed.

def is_pass_or_fail(marks):
    return marks>50
# Test the function
marks=int(input("Enter your marks:"))
if is_pass_or_fail(marks):
    print("Passed")
else:
    print("Failed")