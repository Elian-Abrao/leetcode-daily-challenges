from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # Key insight: For each bit position, count how many numbers have 0 vs 1
        # at that position. The contribution to total distance from that bit is
        # (count of 0s) * (count of 1s), since every 0-1 pair differs at that bit.
        
        # Edge case: if array is too small, no pairs exist
        if len(nums) <= 1:
            return 0
        
        n = len(nums)
        total_distance = 0
        
        # Since nums[i] <= 10^9 < 2^30, we need at most 30 bits
        # We iterate through each bit position from 0 to 29
        for bit_pos in range(30):
            ones_count = 0
            
            # Count how many numbers have bit set to 1 at position bit_pos
            for num in nums:
                if num & (1 << bit_pos):
                    ones_count += 1
            
            # Numbers with bit = 0 at this position
            zeros_count = n - ones_count
            
            # Each pair (one with 0, one with 1) contributes 1 to the distance
            # Total pairs with differing bits at this position: zeros_count * ones_count
            total_distance += zeros_count * ones_count
        
        return total_distance