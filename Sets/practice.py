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


# Remove Multiple Elements

numbers = {1, 2, 3, 4, 5}
# Remove multiple elements using difference_update
numbers.difference_update({2, 3})
print(numbers)



# Find Students Who Play Either Cricket or Football but Not Both

cricket = {"John", "Alex", "Sam", "Mike"}
football = {"Alex", "Mike", "Bob", "Tom"}
# Symmetric difference
only_one_game = cricket ^ football  # ^ finds students who play only one of the games.
print(only_one_game)   



# Remove Common Elements from Two Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Remove common elements from both sets
A_only = A - B
B_only = B - A
print("A after removing common:", A_only)
print("B after removing common:", B_only)



# Find Non-Repeating Characters in a String
text = "Neelaveni"
# Set of all characters
all_chars = set(text)
# Set of duplicate characters
duplicates = {ch for ch in text if text.count(ch) > 1}
# Non-repeating = all - duplicates
unique_chars = all_chars - duplicates
print(unique_chars)



# Find Common Languages Known by All Employees

employees = [
    {"Python", "Java", "C++"},
    {"Python", "C"},
    {"Python", "Java", "C"}
]
# Find languages everyone knows → intersection of all sets
common_languages = set.intersection(*employees) #set.intersection(*employees) finds common elements across all sets.
print("Common languages:", common_languages)
print("Common languages:", common_languages)



# Find Users Active on Both Websites

site_A_users = {"A101", "A102", "A103", "A104"}
site_B_users = {"A103", "A104", "A105"}
active_on_both = site_A_users & site_B_users # intersection
print("Users on both sites:", active_on_both)
