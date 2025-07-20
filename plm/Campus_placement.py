# p1

##--- From 'a3b2c1' → Output: 'aaabbc'
s = 'a3b2c1'
output = '' #--- no space

for i in range(0, len(s), 2):
    char = s[i]
    count = int(s[i+1])
    output += char * count

print(output)
### o/p: aaabbc

# Each step explaination 
# for i in range(0, len(s), 2): --- why 2
# A: i = 0, 2, 4 ... 0 = a,2 = b, 4 = 1 ---  to pick only the characters (letters)
# char = s[i] (get letter)
# count = int(s[i+1]) (get number right after letter) -- next number
# multiply number with letter in n times(number)

# P2

##--- Check if a Number is a Duck Number
# A Duck number contains 0 but not at the beginning
# Examples: 3210 → Duck, 0123 → Not Duck

def is_duck_number(num_str): # --- 1 --- prefer this 
    return num_str[0] != '0' and '0' in num_str
num = input("Enter a number: ")
if is_duck_number(num):
    print("Duck Number")
else:
    print("Not a Duck Number")

### o/p: Enter a number: 065
# Not a Duck Number

# Code Without Function --- 2
num = input("Enter a number: ")

if num[0] != '0' and '0' in num:
    print("Duck Number")
else:
    print("Not a Duck Number")

# p3

###--- reverse a string 
#1 One-liner Input & Reverse:

# or

# Reverse the letters in each word in a sentence without changing the position of the words 

print(input("Enter a word: ")[::-1])
### Enter a word: 123
# 321
#2 Using Slicing (Most Efficient & Recommended)
s = "hello"
reversed_s = s[::-1]
print(reversed_s)  # Output: olleh

#3 Using reversed() and join()
s = "hello"
reversed_s = ''.join(reversed(s))
print(reversed_s)  # Output: olleh
# reversed("hello") → 'o', 'l', 'l', 'e', 'h'
# ''.join(...) → joins those characters together with no space between (since we use an empty string '').

#4 Using a Loop
s = "hello"
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)  # Output: olleh
# 'h', 'eh', 'leh',  'lleh', 'olleh'


# p4

###--- 18. Check if a number is spy number or not 
# A number is spy if sum and product of its digits are equal.
# Example: 123 → sum=6, product=6 → spy

# Explaination -- 123 → 1 + 2 + 3 = 6 and 1 × 2 × 3 = 6 → ✅ Spy

num = input("Enter a number: ")

sum_digits = 0
prod_digits = 1

for digit in num:
    d = int(digit) #--- remember
    sum_digits += d
    prod_digits *= d

if sum_digits == prod_digits:
    print("Spy Number")
else:
    print("Not a Spy Number")

# p5
###--- 17. Print numbers from 1 to N:
#"Fizz" for multiples of 3
# "Buzz" for multiples of 5
# "FizzBuzz" for both


N = int(input("Enter N: "))

for i in range(1, N + 1): # --- remember this
    if i % 3 == 0 and i % 5 == 0: # --- i
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# p6
###---- Take a sentence as an input, & return the longest word in that sentence

sentence = input("Enter a sentence: ")
words = sentence.split()

longest_word = max(words, key=len)

print("Longest word:", longest_word)

# key=len tells Python to compare the items based on their length instead of their default value.

# p7
###--- Count no of vowels in the word
word = input("Enter a word: ").lower()
vowels = "aeiou"
count = 0

for char in word:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

# p8 
###--- Magic Number Guess (in the code, set some number as magic number. ex:7 
# so until user enters 7 , the answer is not correct ) 

magic_number = 7

while True:
    guess = int(input("Guess the magic number: "))
    if guess == magic_number:
        print("🎉 Correct! You found the magic number.")
        break
    else:
        print("❌ Wrong guess. Try again!")
# while True → infinite loop until break

# p9
# Convert sentence into Title Case 
# ( hello world -> Hello World ) 

# with method

sentence = input("Enter a sentence: ")
title_case = sentence.title()
print("Title Case:", title_case)

# without methods

sentence = input("Enter a sentence: ")
words = sentence.split()
title_case = ""

for word in words:
    if len(word) > 0:
        first_letter = word[0].upper()
        rest = word[1:].lower()
        title_case += first_letter + rest + " "

print("Title Case:", title_case.strip())

# P10 
# Second largest number in the list (without using sort function) 
numbers = [12, 45, 67, 89, 23, 89, 34]

largest = second_largest = float('-inf')  # Step 1

for num in numbers:                        # Step 2
    if num > largest:                      # Step 3
        second_largest = largest          # Step 4
        largest = num                     # Step 5
    elif num > second_largest and num != largest:  # Step 6
        second_largest = num             # Step 7

print("Second largest number:", second_largest)  # Step 8

# Step 1: We initialize both largest and second_largest to negative infinity, so any real number will be greater than them.
# This helps us correctly compare the first few numbers.

#  Step 2: Start looping through each number in the list one by one.
# Step 3: If the current number is greater than the current largest, that means we found a new largest number.
# Step 4: Before updating largest, we move the current largest to second_largest, because it's now the second best.
# Step 5: Now we update largest to the current number.
# Step 6: If the current number is not the largest, but still greater than the second largest, then update second_largest.
# Step 7:  We store the current number as the new second largest.

# p11

###--- Take a word as an input and wherever a vowel is present, replace it with a star. ( maa -> m**) 

word = input("Enter a word: ")
vowels = "aeiouAEIOU"
new_word = ""

for char in word:
    if char in vowels:
        new_word += "*"
    else:
        new_word += char

print("Output:", new_word)

### Enter a word: sfccvaioufd
# sfccv****fd
# p12

###---- Sorting list without using sort function 

# Using Bubble Sort:
numbers = [12, 4, 56, 1, 23, 9]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1): # n - i -1 -- back 
        if numbers[j] > numbers[j + 1]: # number & next number
            # Swap
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)


# p13 --- do more
###---- Count how many times each letter occurs in the word (“maa” - m occurs 1 time a occurs 2 times) 
word = input("Enter a word: ")
frequency = {}

for char in word:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for key in frequency:
    print(f"{key} occurs {frequency[key]} time(s)")
    
## Enter a word: xfvseccv
## x occurs 1 time(s)
## f occurs 1 time(s)
## v occurs 2 time(s)
## s occurs 1 time(s)
## e occurs 1 time(s)
## c occurs 2 time(s)

# p14
###---- Sum of digits of a number 
num = input("Enter a number: ")
sum_digits = 0

for digit in num:
    sum_digits += int(digit)

print("Sum of digits:", sum_digits)


# p15
###---- Find largest or smallest element
numbers = [12, 45, 23, 89, 5, 66]

# Initialize with first element
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest element:", largest)
print("Smallest element:", smallest)


# p16
####---- Count characters in a string 

text = input("Enter a string: ")
count = 0

for char in text:
    count += 1

print("Total characters:", count)


# p17
###--- Remove duplicates 
text = input("Enter a string: ")
result = ""

for char in text:
    if char not in result:
        result += char

print("After removing duplicates:", result)


# p18
###---  Sum of even & sum of odd numbers in the list ( 1,3,5,78,8,2,4) 
numbers = [1, 3, 5, 78, 8, 2, 4]

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of Even Numbers:", even_sum)
print("Sum of Odd Numbers:", odd_sum)


# p19
###--- Fibonacci Series 
n = int(input("Enter how many Fibonacci numbers you want: "))

a = 0
b = 1

print("Fibonacci Series:")

for _ in range(n):
    print(a, end=' ')
    c = a + b
    a = b
    b = c


# p20
###--- Checking if a number is prime or not 
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")





