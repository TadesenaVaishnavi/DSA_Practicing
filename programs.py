#1)Find Median of the given Array
# Example 1:
# Input:
#  [2,4,1,3,5]
# Output:
#  3

# Example 2:
# Input:
#  [2,5,1,7]
# Output:
#  3.5
# odd -- middle number
# even -- avg of middle 2 numbers
# Function to calculate the median of the array
def getMedian(arr, n):
    arr.sort()  # Sort the array to arrange elements in order
    
    if n % 2 == 0:
        # If the array size is even, calculate the average of two middle elements
        ind1 = (n // 2) - 1
        ind2 = (n // 2)
        print((arr[ind1] + arr[ind2]) / 2)  # Return the median for even-sized array
    else:
        # If the array size is odd, return the middle element
        print(arr[n // 2])

# Driver code
arr = [4, 7, 1, 2, 5, 6]
n = 6
print("The median of the array is: ", end="")
getMedian(arr, n)  # Function call to calculate and print the median


# So median = average of 4 and 6


# 2) Remove Duplicates From an Unsorted Array

# Solution class
class Solution:
    # Function to remove duplicates from an array
    def remove_duplicates(self, arr):
        # List to store unique elements
        result = []

        # Traverse each element in arr
        for i in range(len(arr)):
            # Flag to check if element already exists in result
            found = False

            # Check for duplicates in result
            for j in range(len(result)):
                if arr[i] == result[j]:
                    found = True
                    break

            # If not found, append to result
            if not found:
                result.append(arr[i])

        # Return the result
        return result

# Main function
def main():
    # Input array
    arr = [4, 5, 4, 2, 2, 3, 1]

    # Create Solution object
    sol = Solution()

    # Call remove_duplicates
    result = sol.remove_duplicates(arr)

    # Print result
    print("Array after removing duplicates:", result)

# Run main
main()


# Solution class containing optimized method
class Solution:
    # Method to remove duplicates from array
    def remove_duplicates(self, arr):
        seen = {}
        result = []

        # Traverse each element
        for val in arr:
            # If not already seen, add to result
            if val not in seen:
                result.append(val)
                seen[val] = True

        return result

# Driver code
if __name__ == "__main__":
    arr = [4, 5, 4, 2, 2, 3, 1]
    sol = Solution()
    result = sol.remove_duplicates(arr)
    print("Array after removing duplicates:", result)
