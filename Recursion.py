# RECURSION:
# Recursion is a programming technique where a function calls itself to solve a problem step-by-step until a base condition is reached.
# In simple words:
#  A function solving a problem by breaking it into smaller versions of the same problem.

# Two Important Parts of Recursion
# Base Case:
# Stops the recursion (prevents infinite calls)

# Recursive Case:
# The function calls itself with a smaller input


#1. Print numbers from 1 to N
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)
print_1_to_n(5)







