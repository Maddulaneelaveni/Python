# What is a Generator?
# Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.

# A Generator is a special type of function that:
# Uses yield instead of return
# Produces values one at a time
# Remembers its state between calls
# Is memory efficient
# 👉 Instead of returning all values at once, it generates values lazily (on demand).

# example :
def my_generator():
  yield 1
  yield 2
  yield 3
for value in my_generator():
  print(value)
# Output:
# 1
# 2
# 3

# Normal Function vs Generator :
# Normal Function:

