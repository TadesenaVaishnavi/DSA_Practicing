##-- A string is a sequence of characters, usually enclosed in quotes.
#Python:
name = "Vaishnavi"
#C:
char name[] = "Vaishnavi";
#Java:
String name = "Vaishnavi";
# Strings are immutable in Python/Java
s = "hello"
s[0] → 'h'
s[-1] → 'o'

# String Traversal
for ch in "hello":
    print(ch)

# Length: len(s)

# Concatenation: "hello" + "world"

# Substring: s[1:4] → "ell"

# Reverse: s[::-1]

# Check membership: 'a' in "apple"


# Character Frequency
from collections import Counter
freq = Counter("hello")
# freq = {'h':1, 'e':1, 'l':2, 'o':1}


# Two-Pointer Technique
# Used in palindrome, substring search, sliding window.
def is_palindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
# String Comparison
# Useful in sorting, anagram problems, substring checks.
sorted("listen") == sorted("silent")  # anagram check

# String to Number / Number to String
int("123") → 123
str(456) → "456"

# Sliding Window Technique
# Pattern Matching / Substrings
# Logic Building Strategy


#---> Example Problems

# Find the first non-repeating character in "aabbcde".

from collections import Counter
s = "aabbcde"
freq = Counter(s)
for ch in s:
    if freq[ch] == 1:
        print(ch)  # Output: c
        break
# Reverse a String -- Concept: Traversal / slicing.

s = "hello"
print(s[::-1])

# Check Palindrome -- Input: "madam" → Output: True

def is_palindrome(s):
    return s == s[::-1]








