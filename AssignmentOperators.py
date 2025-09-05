# Assignment operators are used to assign values to variables.
# Include =, +=, -=, *=, /=, %=, **=, //=
# banking apps, score tracking in games.


# Problems

# 1. Assign a value to a variable and perform +=,*=, and -= operations
x = 10
x += 5
print("x after += 5:", x)   # 15

x *= 2
print("x after *= 2:", x)   # 30

x -= 10
print("x after -= 10:", x)  # 20


# 2.Bank deposit update (+=)
balance = 1000
deposit = 500
balance += deposit
print("Updated Balance:", balance)  # 1500


# 3.Salary increment (+=)
salary = 30000
salary += 5000
print("New Salary:", salary)  # 35000


# 4.Power calculation (**=)
num = 3
num **= 4
print("3^4 =", num)  # 81


# 5.Cricket score update (+=)
score = 100
six = 6
score += six
print("Updated Score:", score)  # 106


# 6.Bill splitting (//=)
bill = 1200
people = 4
bill //= people
print("Share per person:", bill)  # 300

