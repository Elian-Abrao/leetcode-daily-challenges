class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        # dp[i] = minimum cost to reach step i before paying its cost.
        # Steps 0 and 1 are free starting points.
        dp_prev2 = 0  # dp[i - 2]
        dp_prev1 = 0  # dp[i - 1]

        for i in range(2, n + 1):
            current = min(dp_prev1 + cost[i - 1], dp_prev2 + cost[i - 2])
            dp_prev2, dp_prev1 = dp_prev1, current

        return dp_prev1