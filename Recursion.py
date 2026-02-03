# RECURSION:
# Recursion is a programming technique where a function calls itself to solve a problem step-by-step until a base condition is reached.
# In simple words:
#  A function solving a problem by breaking it into smaller versions of the same problem.

# Two Important Parts of Recursion
# Base Case:
# Stops the recursion (prevents infinite calls)

# Recursive Case:
# The function calls itself with a smaller input
# Missing base case = infinite recursion

# Types of Recursion:

# 1.Direct Recursion :Function calls itself directly

# 2.Indirect Recursion: Function A → Function B → Function A

# 3.Tail Recursion: Recursive call is the last statement

# 4.Non-Tail Recursion: Code exists after recursive call

# Why Base Case Is CRITICAL?

# Base case stops recursion

Without it → infinite calls

Infinite calls → stack keeps growing

Memory fills → 💥 Stack Overflow Error


#1. Print numbers from 1 to N
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)
print_1_to_n(5)

# 2. Print numbers from N to 1
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)

print_n_to_1(5)





