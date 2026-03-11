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

# INTERMEDIATE LEVEL

# 4. Find the first non-repeating character in a string
s = "swiss"
char_count = {}
for ch in s:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1
first_non_repeating = None
for ch in s:
    if char_count[ch] == 1:
        first_non_repeating = ch
        break   
print("First non-repeating character:", first_non_repeating)
# Output: "w"

# 5. Check if two strings are anagrams
s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("Anagrams: True")
else:
    print("Anagrams: False")
# Output: True

# 6. Remove duplicates from a string
s = "banana"
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("String after removing duplicates:", result)
# Output: "ban"

# ADVANCED LEVEL
# 7. Find the longest substring without repeating characters
s = "abcabcbb"
start = 0
max_length = 0
used_char = {}
for i, ch in enumerate(s):
    if ch in used_char and start <= used_char[ch]:
        start = used_char[ch] + 1
    else:
        max_length = max(max_length, i - start + 1)
    used_char[ch] = i


# 8. Validate parentheses in a string : 

def brackets(s):
    stack = []
    for c in s:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if (c == ')' and top != '(') or \
               (c == '}' and top != '{') or \
               (c == ']' and top != '['):
                return False
    return len(stack) == 0
print(brackets("[{}()]"))   # True
print(brackets("[(])"))    # False

# 9. If n=3, generate all combinations of well-formed parentheses :

def generate(n):
    result = []
    def solve(s, open, close):
        if len(s) == 2*n:
            result.append(s)
            return 
        if open < n:
            solve(s + "(", open + 1, close) 
        if close < open:
            solve(s + ")", open, close + 1)
    solve("", 0, 0)
    return result
print(generate(3))