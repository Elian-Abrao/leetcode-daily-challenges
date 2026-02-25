from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Use a sliding window to maintain a contiguous subarray whose sum is >= target.
        Expand the right end to grow the sum, and shrink from the left when the sum
        meets or exceeds the target, updating the minimal length accordingly.
        Time: O(n), Space: O(1)
        """
        n = len(nums)
        if n == 0:
            return 0

        left = 0
        current_sum = 0
        # Initialize with a value larger than any possible subarray length
        min_len = n + 1

        for right in range(n):
            current_sum += nums[right]

            # Try to shrink the window from the left while maintaining sum >= target
            while current_sum >= target:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                current_sum -= nums[left]
                left += 1

        return 0 if min_len == n + 1 else min_len