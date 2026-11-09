from __future__ import annotations

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        # Edge case: empty array (though constraints say length >= 1, we handle defensively)
        if not nums:
            return 0
        
        # Track the maximum length seen so far
        max_length = 1
        # Current streak length (at least 1, since a single element is trivially increasing)
        current_streak = 1
        
        # Scan the array, tracking consecutive increasing pairs
        # When nums[i] > nums[i-1], we extend the current streak
        # Otherwise, we reset the streak to 1 at position i
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_streak += 1
                # Update global maximum as we go
                if current_streak > max_length:
                    max_length = current_streak
            else:
                # Streak broken: reset to include only the current element
                current_streak = 1
        
        return max_length