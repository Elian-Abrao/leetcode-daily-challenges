from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Count all arithmetic subsequences of length >= 3.
        For each index i, dp[i] maps a difference 'diff' to the number of
        arithmetic subsequences ending at i with that common difference
        and length >= 2. The answer accumulates the count of extensions that
        produce length >= 3.
        """
        n = len(nums)
        if n < 3:
            return 0

        # dp[i] : dict{diff: count_of_subseq_of_len_ge_2_ending_at_i}
        dp = [defaultdict(int) for _ in range(n)]

        total = 0  # count of all arithmetic subsequences (length >= 3)

        for i in range(n):
            # For each previous index j, compute the difference
            for j in range(i):
                diff = nums[i] - nums[j]   # may be large; Python int is fine

                # Number of subsequences ending at j with this diff (length >= 2)
                prev = dp[j].get(diff, 0)

                # Extend all those subsequences -> they become length >= 3
                total += prev

                # Add the pair (j, i) as a new length-2 subsequence
                dp[i][diff] += prev + 1

        return total