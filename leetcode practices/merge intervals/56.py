from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            # If merged list is empty or no overlap, just append
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged


sol = Solution()
print(sol.merge([[1,4],[2,5],[7,9]]))  
# Output: [[1,5],[7,9]]
