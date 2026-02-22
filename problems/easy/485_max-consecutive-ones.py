from __future__ import annotations
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Initialize two counters:
        # cur tracks the length of the current run of 1s.
        # max_len tracks the maximum run length observed so far.
        max_len = 0
        cur = 0

        for val in nums:
            if val == 1:
                cur += 1
                if cur > max_len:
                    max_len = cur
            else:
                # Reset current run when we see a 0
                cur = 0

        return max_len