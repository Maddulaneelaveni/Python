# 1.Remove Duplicates from a List
numbers=[1, 2, 2, 3, 4, 4, 5]
# Convert list to set to remove duplicates
unique_numbers = set(numbers)
# Convert back to list if needed
unique_list = list(unique_numbers)
print(unique_list)

# set(numbers) removes duplicates.
# list() converts set back to a list.


# 2.Find Common Elements Between Two Sets

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Common elements using intersection
common = A & B
print(common)



