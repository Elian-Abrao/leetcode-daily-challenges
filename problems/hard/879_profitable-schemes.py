class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        MOD = 10**9 + 7

        # Only keep crimes that are possible with the available members
        valid_profits = [p for g, p in zip(group, profit) if g <= n]

        # dp[k] = number of ways to achieve total profit (capped at minProfit) exactly k
        dp = [0] * (minProfit + 1)
        dp[0] = 1

        for p in valid_profits:
            for k in range(minProfit, -1, -1):
                new_k = min(minProfit, k + p)
                dp[new_k] = (dp[new_k] + dp[k]) % MOD

        # dp[minProfit] holds the number of schemes with total profit >= minProfit
        return dp[minProfit]