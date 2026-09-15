from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Binary search on indices.
        # Key insight: before the single element, every pair starts at an even index.
        # After the single element, every pair starts at an odd index.
        lo, hi = 0, len(nums) - 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            # If mid is odd, move it to the even position of its pair
            if mid % 2 == 1:
                mid -= 1
            
            # If the pair is intact, the single element is on the right half
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                # Pair broken, single element is on the left half (including mid)
                hi = mid
        
        return nums[lo]