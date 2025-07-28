# Array concepts & programs
# An array is a collection of elements (usually of the same data type) stored in contiguous memory locations.
arr = [45,87,98,35]

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

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
print(*arr)

