
# in online python interpreter

def trap(height):
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water = right_max - height[right]
            right -= 1
    return water
    


input_str = input("Enter height with space b/w them: ")

height = list(map(int, input_str.strip().split()))
result = trap(height)
print("Total water trapped: ",result)




# output
# Enter height with space b/w them: 4 2 0 3 2 5
# Total water trapped:  9


# in leekcode 
# class Solution:
#  def trap(self, height: List[int]) -> int:



# Comments 
# def trap(height):
#     # Initialize two pointers: left (start) and right (end)
#     left, right = 0, len(height) - 1

#     # Variables to keep track of the maximum height seen so far from left and right
#     left_max, right_max = 0, 0

#     # Variable to store the total amount of trapped water
#     water = 0

#     # Loop until the two pointers meet
#     while left < right:
#         # Compare the height at both ends
#         if height[left] < height[right]:
#             # If current height is greater than or equal to left_max, update left_max
#             if height[left] >= left_max:
#                 left_max = height[left]
#             else:
#                 # Otherwise, water can be trapped above the current bar
#                 water += left_max - height[left]
#             # Move the left pointer to the right
#             left += 1
#         else:
#             # If current height is greater than or equal to right_max, update right_max
#             if height[right] >= right_max:
#                 right_max = height[right]
#             else:
#                 # Otherwise, water can be trapped above the current bar
#                 water += right_max - height[right]
#             # Move the right pointer to the left
#             right -= 1

#     # Return the total amount of water trapped
#     return water
