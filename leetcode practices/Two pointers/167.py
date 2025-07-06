from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        left = 0                          # Start from the beginning of the list
        right = len(numbers) - 1         # Start from the end of the list

        # Loop until the two pointers meet
        while left < right:
            # Calculate the sum of the two numbers pointed to by left and right
            current_sum = numbers[left] + numbers[right]

            # If the sum matches the target, return their positions (1-based)
            if current_sum == target:
                return [left + 1, right + 1]  # Add 1 because LeetCode expects 1-based indices

            # If the sum is too small, move the left pointer to the right to increase the sum
            elif current_sum < target:
                left += 1

            # If the sum is too large, move the right pointer to the left to decrease the sum
            else:
                right -= 1

        # If no valid pair is found (shouldn't happen as per LeetCode constraints), return an empty list
        return []

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]

# o/p:[1,2]




#your output program
# class Solution:
#     def twoSum(self, numbers, target):
#         left = 0
#         right = len(numbers) - 1

#         while left < right:
#             current_sum = numbers[left] + numbers[right]
            
#             if current_sum == target:
#                 return [left + 1, right + 1]
#             elif current_sum < target:
#                 left += 1
#             else:
#                 right -= 1

#         return []

# # Create an instance of the class
# sol = Solution()

# # Now call the method correctly
# numbers = [1, 3, 5, 7]
# target = 6
# output = sol.twoSum(numbers, target)

# print(output)  # Output: []





# another question dt find

# Find All Index Pairs That Add to Target (1-based indexing):
# python
# Copy code


# def findAllPairs(numbers, target):
#     pairs = []
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 pairs.append([i + 1, j + 1])  # 1-based indexing
#     return pairs
# numbers = [1, 3, 5, 5, 7]
# target = 6

# print(findAllPairs(numbers, target))

# o/p:- [[1, 3], [1, 4]]

# ---numbers = [1, 1, 5, 5, 7]
# target = 6
# o/p:-[[1, 3], [1, 4], [2, 3], [2, 4]]