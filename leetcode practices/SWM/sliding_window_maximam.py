from collections import deque
# from typing import List -- leekcode


# class Solution: ---- leekcode
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
 

def sliding_window_maximum(nums, k):
    if not nums:
        return []

    result = []
    dq = deque()  # stores indices

    for i in range(len(nums)):
        # Remove indices that are out of this window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements smaller than the current element from the back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Append the max value (at the front of the deque) once the first window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# --- Taking input from the user ---

# Input format: space-separated integers
nums = list(map(int, input("Enter the array elements (space-separated): ").split()))
k = int(input("Enter the window size (k): "))

# Call the function and print the result
output = sliding_window_maximum(nums, k)
print("Sliding window maximums:", output)



