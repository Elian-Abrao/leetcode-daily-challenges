from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Key insight: track both max and min products ending at current position
        # because a negative number can flip min to max and vice versa
        
        # Edge case: single element
        if len(nums) == 1:
            return nums[0]
        
        # Initialize with first element
        global_max = nums[0]
        current_max = nums[0]  # max product ending at current position
        current_min = nums[0]  # min product ending at current position
        
        # Iterate through remaining elements
        for i in range(1, len(nums)):
            num = nums[i]
            
            # If num is negative, it will flip max and min
            # So we need to consider all three cases:
            # 1. Start fresh from current num
            # 2. Multiply with previous max (becomes min if num < 0)
            # 3. Multiply with previous min (becomes max if num < 0)
            
            # Store current_max before updating since we need it for current_min
            temp_max = current_max
            
            # Update max: either start fresh, or extend previous max/min
            current_max = max(num, num * current_max, num * current_min)
            
            # Update min: either start fresh, or extend previous max/min
            current_min = min(num, num * temp_max, num * current_min)
            
            # Update global maximum
            global_max = max(global_max, current_max)
        
        return global_max