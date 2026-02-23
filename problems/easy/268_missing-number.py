from __future__ import annotations
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR approach: combine all indices [0..n-1] with all values in nums,
        # the result will be the missing number, after also XOR-ing with n.
        # This works in O(n) time and O(1) extra space and handles edge cases nicely.
        n = len(nums)
        missing = 0
        for i in range(n):
            missing ^= i        # cancel out index i
            missing ^= nums[i]  # cancel out the value present at index i
        missing ^= n            # account for the extra number n in the full range
        return missing