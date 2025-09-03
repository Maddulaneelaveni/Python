# 1. # 20. Set type
s = {1, 2, 3}
print(type(s))   

# 2. Add element
s.add(4)
print(s)   

# 3. Remove element
s.remove(2)
print(s)   

# 4. Remove duplicates from list
dup_list = [1, 2, 2, 3, 3, 3]
print(set(dup_list))   # prints {1, 2, 3}
