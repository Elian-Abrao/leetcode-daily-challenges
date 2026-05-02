from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two-pointer approach: one to track where to place next non-zero,
        # one to scan through the array
        # Invariant: all elements before `left` are non-zero and in original order
        left = 0
        
        # Iterate through array with right pointer
        for right in range(len(nums)):
            # When we find a non-zero element
            if nums[right] != 0:
                # Swap it with the position at left pointer
                # This maintains relative order of non-zero elements
                nums[left], nums[right] = nums[right], nums[left]
                # Move left pointer forward to next position to fill
                left += 1
        
        # After loop completes:
        # - All non-zero elements are at the front in original order
        # - All zeros are at the end (swapped during the process)
        # Time: O(n), Space: O(1)