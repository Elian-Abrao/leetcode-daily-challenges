from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Key insight: assign + to some numbers (set P) and - to others (set N)
        # sum(P) - sum(N) = target
        # sum(P) + sum(N) = sum(nums)
        # Adding these: 2 * sum(P) = target + sum(nums)
        # So sum(P) = (target + sum(nums)) / 2
        # Problem reduces to: count subsets with sum = (target + total) / 2
        
        total = sum(nums)
        
        # Check if solution is possible
        # 1. (target + total) must be even for integer division
        # 2. target cannot exceed total (all positive) or -total (all negative)
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0
        
        subset_sum = (target + total) // 2
        
        # Edge case: if subset_sum is negative, no solution exists
        if subset_sum < 0:
            return 0
        
        # DP approach: count number of subsets that sum to subset_sum
        # dp[s] = number of ways to achieve sum s
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # One way to make sum 0: select nothing
        
        # Process each number in nums
        for num in nums:
            # Traverse backwards to avoid using the same element twice
            # For each existing sum s, we can add num to create sum s+num
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[subset_sum]