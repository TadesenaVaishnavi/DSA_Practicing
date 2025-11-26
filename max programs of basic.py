# 1) Print Second Largest Number (NO built-in sort / max)

def second_largest(nums):
    first = second = float('-inf')

    for n in nums:
        if n > first:
            second = first
            first = n
        elif first > n > second:
            second = n
    return second

print(second_largest([10, 5, 20, 8, 15]))

# first > n > second: -- less than first number but great than second number so, replace with second number

# 2. Check Palindrome (string or number)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome(121))

# [start : stop : step]

# 3. Count Vowels in a String

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for c in s if c in vowels)

print(count_vowels("Cognizant"))

# 4. Reverse Each Word in a Sentence

def reverse_words(s):
    return " ".join(word[::-1] for word in s.split())

print(reverse_words("welcome to cognizant"))

# (or)
s = "hello world python"
print(' '.join([w[::-1] for w in s.split()]))  # <-- if join was allowed


#without join
sentence = "hello world python"
words = sentence.split()

result = ""
for w in words:
    result += w[::-1] + " "

print(result.strip())

#Using print with end (NO join & NO extra variable)
sentence = "hello world python"
for w in sentence.split():
    print(w[::-1], end=" ")
#Using list indexing (NO join)
sentence = "hello world python"
words = sentence.split()

for i in range(len(words)):
    words[i] = words[i][::-1]

print(*words)   # prints with space


# 5. Remove Duplicates from List (keep order)

def remove_duplicates(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

print(remove_duplicates([1,2,2,3,1,4]))

# 6. Fibonacci Using Recursion(0, 1, 1, 2, 3, 5...)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))

#Basic Fibonacci Series (Loop)
n = int(input("Enter n: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Fibonacci Series Using Recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = 6
for i in range(n):
    print(fib(i), end=" ")
  
#Fibonacci Series Using List
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

print(fibonacci(10))

# 7. Factorial (Iterative)

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))

# 8. Find Sum of Digits

def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

print(sum_digits(987))

# 9. Check if a Number is Armstrong
# 153 -> 1^3+5^3+3^3 =153 ✔)

num = int(input("Enter a number: "))
sum = 0
temp = num
digits = len(str(num))  # number of digits

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")

#Armstrong Using Recursion (Advanced / Interview style)

def sum_power_digits(n, digits):
    if n == 0:
        return 0
    return (n % 10) ** digits + sum_power_digits(n // 10, digits)

def is_armstrong(n):
    digits = len(str(n))
    return n == sum_power_digits(n, digits)

print(is_armstrong(9474))  # True

# 10. Check if a Number is Perfect(6 → divisors: 1, 2, 3 → sum = 6 ✔)

num = int(input("Enter a number: "))
sum_div = 0

for i in range(1, num):
    if num % i == 0:
        sum_div += i

if sum_div == num:
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is NOT a Perfect number")

# 11. Check if a Number is a Strong Number
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
sum_fact = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_fact += factorial(digit)
    temp //= 10

if sum_fact == num:
    print(f"{num} is a Strong number")
else:
    print(f"{num} is NOT a Strong number")

#Using Function for Reusability
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def is_strong(num):
    return num == sum(factorial(int(d)) for d in str(num))

print(is_strong(145))  # True
print(is_strong(123))  # False

#12.Check if a Number is Harshad(# 18 → sum of digits = 1 + 8 = 9 → 18 % 9 == 0)
num = int(input("Enter a number: "))
sum_digits = sum(int(d) for d in str(num))

if num % sum_digits == 0:
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is NOT a Harshad number")
  
#Optimized Version (without converting to string)
def is_harshad(n):
    temp = n
    sum_digits = 0
    while temp > 0:
        sum_digits += temp % 10
        temp //= 10
    return n % sum_digits == 0

print(is_harshad(18))  # True

#Using Function
def is_harshad(n):
    return n % sum(int(d) for d in str(n)) == 0

print(is_harshad(18))  # True
print(is_harshad(19))  # False




#13. leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap year")
else:
    print(f"{year} is NOT a Leap year")

#14. Check if a Number is Prime
num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is NOT prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is NOT prime")
            break
    else:
        print(f"{num} is prime")

#15.biggest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} is the biggest")
elif b >= a and b >= c:
    print(f"{b} is the biggest")
else:
    print(f"{c} is the biggest")

#16.Check if a Character is Uppercase or Lowercase
ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print(f"{ch} is Uppercase")
elif 'a' <= ch <= 'z':
    print(f"{ch} is Lowercase")
else:
    print(f"{ch} is not an alphabet")

#Using isupper() and islower() Methods
ch = input("Enter a character: ")

if ch.isupper():
    print(f"{ch} is Uppercase")
elif ch.islower():
    print(f"{ch} is Lowercase")
else:
    print(f"{ch} is not an alphabet")
#Convert String to Uppercase and Lowercase
s = input("Enter a string: ")

print("Uppercase:", s.upper())
print("Lowercase:", s.lower())



#17. Check if a Number is Odd or Even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

#18 swapping 
a, b = b, a
# or
a = a+b
b = a-b
a = a-b
# or
a = a^b
b = a^b
a = a^b
