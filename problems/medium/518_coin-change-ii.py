from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Classic unbounded knapsack counting combinations.
        # dp[i] = number of ways to make amount i using processed coins.
        # Order of loops ensures combinations (not permutations) are counted.
        dp = [0] * (amount + 1)
        dp[0] = 1  # One way to make amount zero: use no coins.

        for coin in coins:
            # For each coin, iterate amount upwards so it can be reused.
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        # dp[amount] holds the total number of combinations.
        return dp[amount]