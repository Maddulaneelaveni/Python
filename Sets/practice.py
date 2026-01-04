# 1.Remove Duplicates from a List
numbers=[1, 2, 2, 3, 4, 4, 5]
# Convert list to set to remove duplicates
unique_numbers = set(numbers)
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


# 3.Remove Multiple Elements

numbers = {1, 2, 3, 4, 5}
# Remove multiple elements using difference_update
numbers.difference_update({2, 3})
print(numbers)



#4. Find Students Who Play Either Cricket or Football but Not Both

cricket = {"John", "Alex", "Sam", "Mike"}
football = {"Alex", "Mike", "Bob", "Tom"}
# Symmetric difference
only_one_game = cricket ^ football  # ^ finds students who play only one of the games.
print(only_one_game)   



# 5.Remove Common Elements from Two Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Remove common elements from both sets
A_only = A - B
B_only = B - A
print("A after removing common:", A_only)
print("B after removing common:", B_only)



# 6.Find Non-Repeating Characters in a String
text = "Neelaveni"
# Set of all characters
all_chars = set(text)
# Set of duplicate characters
duplicates = {ch for ch in text if text.count(ch) > 1}
# Non-repeating = all - duplicates
unique_chars = all_chars - duplicates
print(unique_chars)



# 7.Find Common Languages Known by All Employees

employees = [
    {"Python", "Java", "C++"},
    {"Python", "C"},
    {"Python", "Java", "C"}
]
# Find languages everyone knows → intersection of all sets
common_languages = set.intersection(*employees) #set.intersection(*employees) finds common elements across all sets.
print("Common languages:", common_languages)
print("Common languages:", common_languages)



#8. Find Users Active on Both Websites

site_A_users = {"A101", "A102", "A103", "A104"}
site_B_users = {"A103", "A104", "A105"}
active_on_both = site_A_users & site_B_users # intersection
print("Users on both sites:", active_on_both)



# 9.Identify Customers Who Bought Products from Only One Store

store1 = {"Ram", "Priya", "Arun", "Neha"}
store2 = {"Priya", "Neha", "Kiran", "Meena"}
unique_customers = store1 ^ store2
print("Unique customers:", unique_customers)



# 10.Find Words Appearing in Both Sentences

sentence1 = "My name is neelaveni"
sentence2 = "My name is neelavei and im pursuing btech"
# Convert to sets
set1 = set(sentence1.split())
set2 = set(sentence2.split())
common = set1 & set2 #  Common words
print("Common words:", common)



# 11.Unique Visitors Count Across Multiple Days

day1 = {"user1", "user2", "user3"}
day2 = {"user2", "user4"}
day3 = {"user1", "user5", "user2"}
# Combine all unique visitors
unique_visitors = set.union(day1, day2, day3)
print("Unique visitors:", unique_visitors)
print("Total count:", len(unique_visitors))



# 12.Detect Duplicates in a List using Sets
nums = [10, 20, 30, 10, 40, 20, 50]
duplicates = {n for n in nums if nums.count(n) > 1} #set comprehension

print("Duplicates:", duplicates)

# 13.Find Students Enrolled in All Courses
course1 = {"Alice", "Bob", "Charlie"}
course2 = {"Bob", "Charlie", "David"}
course3 = {"Charlie", "Bob", "Eve"}
all_students = set.intersection(course1, course2, course3)
print("Students in all courses:", all_students)

# 14.Find Elements Present in One Set but Not in Another
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
difference = setA - setB
print("Elements in A not in B:", difference)

# 15.Find Common Interests Among Group Members
member1 = {"music", "sports", "reading"}
member2 = {"reading", "traveling", "music"} 
member3 = {"music", "cooking", "reading"}
common_interests = set.intersection(member1, member2, member3)
print("Common interests:", common_interests)

# 16.Find Unique Hashtags Used in Social Media Posts
posts = [
    "#fun #sun #beach",
    "#travel #fun #adventure",
    "#beach #relaxation #sun"
]
unique_hashtags = set()
for post in posts:
    hashtags = post.split()
    unique_hashtags.update(hashtags)    
print("Unique hashtags:", unique_hashtags)

# 17.Find Employees Working in Both Departments
dept_A = {"E101", "E102", "E103"}
dept_B = {"E102", "E104", "E105"}
common_employees = dept_A & dept_B
print("Employees in both departments:", common_employees)
# 18.Find Products Available in One Store but Not in Another
store_X = {"apple", "banana", "cherry"}
store_Y = {"banana", "dragonfruit", "elderberry"}
