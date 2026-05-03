from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm: classic dynamic programming approach
        # At each position, we decide whether to extend the current subarray
        # or start a new one from the current element
        
        # Track the maximum sum ending at the current position
        current_sum = nums[0]
        
        # Track the global maximum sum seen so far
        max_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Key decision: either extend the existing subarray or start fresh
            # If current_sum is negative, it will only drag down future sums,
            # so we start a new subarray from nums[i]
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update global maximum if we found a better sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum