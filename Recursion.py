# RECURSION:
# Recursion is a programming technique where a function calls itself to solve a problem step-by-step until a base condition is reached.
# In simple words:
#  A function solving a problem by breaking it into smaller versions of the same problem.

# Interview answer on Recursion:
# In recursion, each function call is stored in the call stack as a separate stack frame.
# The stack follows LIFO order.
# Recursive calls keep pushing frames until the base case is reached.
# Then values return in reverse order, popping stack frames one by one.
# If the base case is missing, the stack keeps growing and causes a stack overflow error.

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
# Without it → infinite calls
# Infinite calls → stack keeps growing
# Memory fills → Stack Overflow Error

# Stack Overflow Error: A stack overflow occurs when the call stack exceeds its maximum memory limit due to too many function calls.

# What is a Call Stack?
# The call stack is a memory structure that stores information about active function calls in a program.
# It follows LIFO (Last In, First Out) order.

# Every time a function is called:
# 1.A stack frame is created
# 2.It is pushed onto the stack
# 3.When the function finishes, its frame is popped from the stack

# What is a Stack Frame?
# Each stack frame contains:
# Function name
# Parameters
# Local variables
# Return address (where to go back after function ends)
# In recursion, many stack frames of the same function are created.


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

# 3. Factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))






