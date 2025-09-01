# 1.Create a variable, assign it the value and Print it
a = 10
print(a)

#2.Assign values to two variables. Print both.
x, y = 10, 20
print(x, y)

#3.Assign the same value  to three variables a, b, c. Print all three.
a = b = c = 8
print(a, b, c)

#4. Assign a number to a variable and then change it to another number.print both.
num = 100
print(num)
num = 200
print(num)

# 5. Assign two numbers to x and y. Assign their sum to z.print z
x, y = 20, 30
z = x + y
print(z)

# 6. Assign one variables value to another.print both
a = 10
b = a
print(a, b)

# Updating Variables
# 7. Assign x=5. Update it as x= x + 2. print the result
x = 5
x = x + 2
print(x)

# 8. Assign a = 2.Cube it by updating the same variable.print
a = 2
a = a ** 3
print(a)

# Swapping and Reassigning
#9. Assign two variables and swap them using a temporary variable
a, b = 5, 10
temp = a
a = b
b = temp
print(a, b)

# 10. Swap two variables without using a third variable
x, y = 3, 4
x, y = y, x
print(x, y)

# 11. Assign a=1,b=2,c=3. Rotate their values (a->b, b->c, c->a).print
a, b, c = 1, 2, 3
a, b, c = b, c, a
print(a, b, c)

# Mathematical Reassignments
# 12. Assign a=10 Update it as a = a%2. print
a = 10
a = a % 2
print(a)

# Increment and Decrement
# 13. Assign score = 0. Increase it by 5, then decrease it by 2. print
score = 0
score = score + 5
score = score - 2
print(score)

# 14. ASsign count = 1. Multiply it by 10, then divide by 5. print
count = 1
count = count * 10
count = count / 5
print(count)

# 15. Assign a = b = 50. change a. print a and b.
a = b = 50
a = 75
print(a, b)






