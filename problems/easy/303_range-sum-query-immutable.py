from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        # Build prefix sum array for O(1) range queries
        # prefix_sum[i] = sum of nums[0:i] (exclusive at i)
        # This allows sumRange(left, right) = prefix_sum[right+1] - prefix_sum[left]
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)
        
    def sumRange(self, left: int, right: int) -> int:
        # Sum from left to right inclusive = prefix_sum[right+1] - prefix_sum[left]
        # prefix_sum[right+1] contains sum up to and including index right
        # prefix_sum[left] contains sum up to but not including index left
        return self.prefix_sum[right + 1] - self.prefix_sum[left]