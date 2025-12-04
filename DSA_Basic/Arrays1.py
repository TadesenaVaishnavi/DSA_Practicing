# Array concepts & programs
# An array is a collection of elements (usually of the same data type) stored in contiguous memory locations.
arr = [45,87,98,35]

# array input in Python
# 1️⃣ Python — Basic Input (Single Line, Space-separated)
# Input: 5 10 15 20
arr = list(map(int, input("Enter array elements: ").split()))
print(arr)
# map(int, ...) → converts each string to integer

# 2️⃣ Python — Input One by One (Using Loop)
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))
print(arr)
# Enter number of elements: 2
# Enter element 1: 3
# Enter element 2: 5
# [3, 5]

# 3️⃣ Python — Input with Comma-separated Values
# Input: 1,2,3,4
arr = list(map(int, input("Enter array elements separated by comma: ").split(',')))
print(arr)

# 4️⃣ Python — Predefined Array (No Input)
arr = [1, 2, 3, 4, 5]
print(arr)

# 5️⃣ Python — Using List Comprehension
arr = [int(x) for x in input("Enter elements: ").split()]
print(arr)

# Enter elements: 5 67 8
# [5, 67, 8]

# Access Example
print(arr[2])
# Indexing starts from 0
# arr[0] → First element
# arr[n-1] → Last element (if n is size)

# Traversal
for i in range(len(arr)):
    print(arr[i])


arr.insert(2, 50) 
arr.pop()       # O(1)
arr.pop(2)      # O(n)
arr.remove(20)  # O(n), searches for the value


# Input/Output Techniques

## Taking input for an array of integers:
arr = list(map(int, input().split()))

## Taking fixed size input:
n = int(input())
arr = list(map(int, input().split()))


print(arr)        # prints full array
# [1, 3, 45, 6, 3, 9]
print(*arr)       # prints space-separated elements
# 1 3 45 6 3 9


# | Operation          | Time Complexity |
# | ------------------ | --------------- |
# | Access by index    | O(1)            |
# | Insert at end      | O(1)\*          |
# | Insert at position | O(n)            |
# | Delete from end    | O(1)            |
# | Delete from middle | O(n)            |
# | Traversal          | O(n)            |


# Array Basics
# Sum of All Elements

n = int(input())
arr = list(map(int, input().split()))
print(sum(arr))


# Find Maximum and Minimum in Array

n = int(input())
arr = list(map(int, input().split()))
print("Max:", max(arr), "Min:", min(arr))

# Insert an Element at a Given Index

arr = [1, 2, 4, 5]
x = 3
k = 2
arr.insert(k, x)
print(arr)

# Delete an Element at a Given Index

arr = [10, 20, 30, 40, 50]
k = 2
arr.pop(k)
print(arr)

# Reverse the Array
# Reverse an Array (Without using built-in reverse)
arr = [1,4,7,3,6,2]
print(arr)

i = 0
j = len(arr) -1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
print(arr)


# with built-in
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
print(*arr)


# Find Max & Min in an Array

arr = [1,3,6,-1,6,33]
maxi = mini = arr[0]
for num in arr:
    if num > maxi:
        maxi = num
    if num < maxi:
        mini = num
print("max:", maxi)
print("min:", mini)

# Two-Sum (Easy Version) 
# Given array + target → return indexes of two numbers that add up to target.
# Example:
# arr = [2, 7, 11, 15], target = 9 → output = [0, 1] -- 2+7 = 9

# Approach 1 — Brute Force (Beginner Friendly)
# Check all pairs → O(n²)
arr = [2, 7, 11, 15]
target = 9

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print([i, j])
            break
# Approach 2 — Hash Map (Best Logic for Interviews)
# Use dictionary to store {value: index}
# For each element check: target - arr[i] already seen?

