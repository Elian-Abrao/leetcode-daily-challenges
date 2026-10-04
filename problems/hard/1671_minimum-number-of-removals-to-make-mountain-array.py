from __future__ import annotations
from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """
        Returns the minimum number of elements to remove so that the remaining
        array forms a mountain (strictly increasing then strictly decreasing).
        """
        n = len(nums)

        # left[i] = length of longest strictly increasing subsequence ending at i
        left = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    left[i] = max(left[i], left[j] + 1)

        # right[i] = length of longest strictly decreasing subsequence starting at i
        # (i.e. increasing when scanning from right to left)
        right = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:          # nums[i] > nums[j] -> decreasing
                    right[i] = max(right[i], right[j] + 1)

        max_mountain_len = 0
        # Peak cannot be at the ends (need at least one element on each side)
        for i in range(1, n - 1):
            if left[i] >= 2 and right[i] >= 2:   # valid peak
                mountain_len = left[i] + right[i] - 1  # peak counted twice
                max_mountain_len = max(max_mountain_len, mountain_len)

        # Minimum removals = total length - longest mountain subsequence
        return n - max_mountain_len