from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search on rotated sorted array
        # Key insight: at least one half of the array is always sorted
        # We can determine which half is sorted by comparing endpoints
        # Then decide which half to search based on target's range
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Found target
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            # Left half is sorted if nums[left] <= nums[mid]
            if nums[left] <= nums[mid]:
                # Left half [left...mid] is sorted
                # Check if target is within this sorted range
                if nums[left] <= target < nums[mid]:
                    # Target is in the sorted left half
                    right = mid - 1
                else:
                    # Target must be in the right half (sorted or not)
                    left = mid + 1
            else:
                # Right half [mid...right] is sorted
                # Check if target is within this sorted range
                if nums[mid] < target <= nums[right]:
                    # Target is in the sorted right half
                    left = mid + 1
                else:
                    # Target must be in the left half (sorted or not)
                    right = mid - 1
        
        # Target not found
        return -1