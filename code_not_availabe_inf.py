# Find all Palindrome Numbers in a given range

# 1 Problem Statement: Given a range of numbers, find all the palindrome numbers in the range.

# Enter start of range: 10
# Enter end of range: 100
# Palindrome numbers in the range:
# 11 22 33 44 55 66 77 88 99 


def is_palindrome(n):
    rev = 0
    temp = n
    
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
        
    return rev == n


def find_palindromes(start, end):
    for num in range(start, end + 1):
        if is_palindrome(num):
            print(num, end=" ")


# Driver code
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Palindrome numbers in the range:")
find_palindromes(start, end)
