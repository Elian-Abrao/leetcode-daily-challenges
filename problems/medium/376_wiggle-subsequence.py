from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # Edge case: single element is trivially a wiggle sequence
        if len(nums) < 2:
            return len(nums)
        
        # Greedy approach: track the length when last difference was positive vs negative
        # up: max length ending with an upward (positive) difference
        # down: max length ending with a downward (negative) difference
        up = 1
        down = 1
        
        # Iterate through adjacent pairs
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # Current element is greater: we can extend a "down" sequence
                # by adding this upward move
                up = down + 1
            elif nums[i] < nums[i - 1]:
                # Current element is smaller: we can extend an "up" sequence
                # by adding this downward move
                down = up + 1
            # If nums[i] == nums[i-1], no change: can't use equal elements in wiggle
        
        # The answer is the maximum of ending with up or down
        return max(up, down)