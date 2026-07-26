from typing import List

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        pair_and_count = {}
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                pair_result = nums[i] & nums[j]
                pair_and_count[pair_result] = pair_and_count.get(pair_result, 0) + 1
        
        total_count = 0
        
        for k in range(len(nums)):
            for pair_and, count in pair_and_count.items():
                if pair_and & nums[k] == 0:
                    total_count += count
        
        return total_count