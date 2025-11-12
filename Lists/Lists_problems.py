# 1. Find the sum of all elements in a list

num=[10, 20, 30, 40]
# sum() is an inbuilt function that adds all elements
total=sum(num)
print("Sum:", total)

# output:
# Sum:100



# 2.Find the largest number in a list

nums = [5, 8, 12, 3, 7]
# max() finds the largest element
largest=max(nums)
print("Largest:", largest)

# output:
# Largest:12



# 3. Reverse a list

nums=[1, 2, 3, 4, 5]
# [::-1] slicing reverses the list
reversed_list=nums[::-1]
print("Reversed:", reversed_list)

# output:
# Reversed: [5, 4, 3, 2, 1]



# 4.Count occurrences of an element

nums = [1, 2, 3, 2, 4, 2]
# count() gives how many times a value appears
count_2 = nums.count(2)
print("Count of 2:", count_2)

# output:
#Count of 2: 3



# 5.Remove duplicates from a list

nums = [1, 2, 2, 3, 4, 4, 5]
# set() removes duplicates, then convert back to list
unique = list(set(nums))
print("Unique:", unique)

# output:
#Unique: [1, 2, 3, 4, 5]



# 6. Find the second largest element

nums = [10, 20, 4, 45, 99]
# Convert to set (to remove duplicates) then sort
unique = sorted(set(nums))
second_largest = unique[-2]   # second from last
print("Second Largest:", second_largest)

# output:
# Second Largest: 45



# 7. Merge two lists

list1=[1, 2, 3]
list2=[4, 5, 6]
# '+' operator joins lists
merged=list1 + list2
print("Merged:", merged)

# output:
# Merged: [1, 2, 3, 4, 5, 6]



# 8.Find common elements in two lists

list1=[1, 2, 3, 4]
list2=[3, 4, 5, 6]
# set intersection finds common values
common=list(set(list1) & set(list2))
print("Common:", common)

# output:
# Common: [3, 4]



# 9.Find elements present in one list but not the other

list1=[1, 2, 3, 4]
list2=[3, 4, 5, 6]
# set difference gives unique items
diff=list(set(list1)-set(list2))
print("Unique in list1:", diff)

# output:
# Unique in list1: [1, 2]



# 10.Rotate a list by k positions

nums=[1, 2, 3, 4, 5]
k = 2
# Take last k elements + first part
rotated=nums[-k:]+nums[:-k]
print("Rotated:", rotated)

# output:
# Rotated: [4, 5, 1, 2, 3]



# 11.Find the index of an element

fruits=["apple", "banana", "cherry", "mango"]
# index() returns the position of the element
index= fruits.index("mango")
print("Index of mango:", index)

# output:
# Index of mango: 3



# 12.Separate even and odd numbers into two lists

nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# List comprehension with condition
evens=[n for n in nums if n % 2 == 0]
odds=[n for n in nums if n % 2 != 0]
print("Evens:", evens)
print("Odds:", odds)

# output:
# Evens: [2, 4, 6, 8]
# Odds: [1, 3, 5, 7, 9]



# 13.Find the frequency of each element in a list

nums=[1, 2, 2, 3, 4, 4, 4, 5]
freq={}
for n in nums:
    freq[n] = freq.get(n, 0) + 1
print("Frequencies:", freq)

# output:
# Frequencies: {1: 1, 2: 2, 3: 1, 4: 3, 5: 1}



# 14.Find the product of all elements

nums=[1, 2, 3, 4]
product=1
for n in nums:
    product *= n   # multiply each element
print("Product:", product)

# output:
# product: 24


# 15.Check if a list is sorted

nums=[1, 2, 3, 4, 5]
# Compare with sorted version
if nums==sorted(nums):
    print("List is sorted")
else:
    print("List is not sorted")

# output:
# List is sorted



# 16.Flatten a Nested List

nested_list=[[1, 2], [3, 4], [5, 6]]
flat_list=[num for sub in nested_list for num in sub]
print("Flattened:", flat_list)
# List comprehension is used here:
# 1.for sub in nested → loops through each inner list
# 2.for num in sub → loops through elements of that inner list
# 3. Collect each 'num' into the final list

# output:
# Flattened: [1, 2, 3, 4, 5, 6]



# 17.Find the Frequency of Each Element

nums=[1, 2, 2, 3, 4, 4, 4, 5]
freq={}
for n in nums: # Loop through each number in the list
    freq[n]=freq.get(n, 0) + 1
print("Frequencies:", freq)
# freq.get(n,0) → gets current count of 'n', default 0 if not found
# Add 1 to the count and update the dictionary

# output:
# Frequencies: {1: 1, 2: 2, 3: 1, 4: 3, 5: 1}




 # 18.Remove All Occurrences of an Element

 nums = [1, 2, 3, 2, 4, 2, 5]
# List comprehension with condition
# It keeps only the numbers that are NOT equal to 2
new_list = [n for n in nums if n != 2]
print("After removing 2:", new_list)

# output:
# After removing 2: [1, 3, 4, 5]




























