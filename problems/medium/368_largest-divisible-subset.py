from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Sorting turns the pairwise divisibility condition into a chain condition:
        # if a divides b and b divides c, then the subset can be built left to right.
        nums.sort()
        n = len(nums)

        # dp[i] = length of the largest divisible subset ending at nums[i].
        dp = [1] * n

        # parent[i] stores the previous index in the chosen chain.
        # -1 means nums[i] starts a subset by itself.
        parent = [-1] * n

        best_len = 1
        best_idx = 0

        for i in range(n):
            # Try to extend every earlier valid chain.
            for j in range(i):
                # Because nums is sorted, checking nums[i] % nums[j] == 0 is enough.
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

            # Track the global best endpoint for reconstruction.
            if dp[i] > best_len:
                best_len = dp[i]
                best_idx = i

        # Reconstruct the subset by following parent links backwards.
        result = []
        while best_idx != -1:
            result.append(nums[best_idx])
            best_idx = parent[best_idx]

        # We collected elements from largest to smallest, so reverse at the end.
        result.reverse()
        return result