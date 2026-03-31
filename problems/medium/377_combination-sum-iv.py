from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Sorting lets us stop early once a number is too large for the current sum.
        nums.sort()

        # dp[current] = number of ordered sequences whose sum is exactly current.
        # The empty sequence is the unique way to build sum 0.
        dp = [0] * (target + 1)
        dp[0] = 1

        # Build answers bottom-up so every smaller subproblem is already known.
        for current in range(1, target + 1):
            total_ways = 0

            # Because order matters, we treat each current sum independently and
            # try every possible last number in the sequence.
            for num in nums:
                if num > current:
                    # Larger numbers cannot contribute to this sum or any later
                    # position in this sorted iteration.
                    break
                total_ways += dp[current - num]

            dp[current] = total_ways

        return dp[target]