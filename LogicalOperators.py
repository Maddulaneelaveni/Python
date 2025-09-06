# Logical operators are used to combine multiple conditions.
# Include and , or, not operators.
# and -> True if both are true
# or -> True if atleast one
# not -> Reverse the result
# used in decision making, login validation and acess control


# problems:


# 1.Assign a value to x and perform and, or, not operations
x = 10
print(x > 5 and x < 20)  # True
print(x > 5 or x > 15)   # True
print(not(x > 5))        # False


# 2. Voting Eligibility 
# Check if a person is eligible to vote (age ≥18 and has voter ID).
age = 20
has_id = True
print("Eligible to vote?", age >= 18 and has_id)  # True


# 3.Check if a number is Divisible by 3 or 5

num = 15
print("Divisible?", num % 3 == 0 or num % 5 == 0)  # True


# 4.Pass if marks in both subjects ≥40
# Verify if a student passes
math = 50
science = 30
print("Passed?", math >= 40 and science >= 40)  # False


# 5.Login check
#Check if a login is valid (username correct and password correct).
username = "admin"
password = "1234"
print("Login successful?", username == "admin" and password == "1234")  # True


# 6.Email validation
# Check if an email is valid (contains "@" and contains ".com").
email = "neelaveni@gmail.com"
print("Valid Email?", "@" in email and ".com" in email)  # True


