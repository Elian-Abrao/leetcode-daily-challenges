from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Binary search approach to find peak in O(log n) time
        # Key insight: If nums[mid] < nums[mid+1], there must be a peak on the right
        # (since nums[n] = -inf, we must eventually go down)
        # Similarly, if nums[mid] > nums[mid+1], there must be a peak on the left or at mid
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Compare mid with its right neighbor
            if nums[mid] < nums[mid + 1]:
                # We're on an ascending slope, peak must be to the right
                # Move left pointer past mid since mid can't be a peak
                left = mid + 1
            else:
                # nums[mid] > nums[mid + 1] (equality impossible per constraints)
                # We're on a descending slope, peak is at mid or to the left
                # Keep mid as potential answer
                right = mid
        
        # When left == right, we've found a peak
        # This works because:
        # - Single element is always a peak (nums[-1] and nums[n] are -inf)
        # - Our binary search invariant guarantees left points to a peak
        return left