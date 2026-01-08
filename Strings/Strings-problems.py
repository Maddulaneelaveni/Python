# BASIC LEVEL

# 1. Reverse a string
s = "hello"
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string:", rev)
# Output: "olleh"

# 2. Check if a string is a palindrome
s = "racecar"
is_palindrome = True   
for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        is_palindrome = False
        break
print("Is palindrome:", is_palindrome)
# Output: True

# 3. Count vowels in a string
s = "hello world"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)
# Output: 3
