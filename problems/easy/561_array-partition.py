from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sorting pairs adjacent numbers ensures the largest possible minimum
        # for each pair, maximizing the total sum.
        nums.sort()
        return sum(nums[::2])