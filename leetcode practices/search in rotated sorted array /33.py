def search(nums, target):
    # Initialize two pointers for binary search
    left, right = 0, len(nums) - 1

    # Continue searching while the search space is valid
    while left <= right:
        # Find the middle index
        mid = (left + right) // 2

        # Check if the middle element is the target
        if nums[mid] == target:
            return mid  # Target found at index mid

        # Determine which half is sorted

        # If the left half (from nums[left] to nums[mid]) is sorted
        if nums[left] <= nums[mid]:
            # Check if target lies within the left sorted half
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Move to the left half
            else:
                left = mid + 1   # Move to the right half

        # Otherwise, the right half (from nums[mid] to nums[right]) is sorted
        else:
            # Check if target lies within the right sorted half
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Move to the right half
            else:
                right = mid - 1  # Move to the left half

    # Target not found in the array
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))  # Output: 4
