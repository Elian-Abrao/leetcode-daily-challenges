from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search to find target or its insert position
        # Time: O(log n), Space: O(1)
        
        left, right = 0, len(nums) - 1
        
        # Standard binary search with modification to track insert position
        while left <= right:
            mid = left + (right - left) // 2  # Avoid potential overflow
            
            if nums[mid] == target:
                # Target found, return its index
                return mid
            elif nums[mid] < target:
                # Target is in the right half
                left = mid + 1
            else:
                # Target is in the left half
                right = mid - 1
        
        # If target not found, left pointer will be at the insert position
        # Invariant: at termination, left > right and left is the smallest index
        # where nums[left] > target (or len(nums) if target > all elements)
        return left