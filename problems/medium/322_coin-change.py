from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Zero amount needs no coins regardless of available denominations.
        if amount == 0:
            return 0

        # Coins larger than the target can never help, so removing them keeps
        # the DP loop smaller without changing correctness.
        usable_coins = [coin for coin in coins if coin <= amount]
        if not usable_coins:
            return -1

        # Use amount + 1 as a safe "infinity" sentinel because no valid answer
        # can require more than `amount` coins when coin value 1 exists.
        unreachable = amount + 1
        dp = [unreachable] * (amount + 1)
        dp[0] = 0

        # Unbounded knapsack DP:
        # dp[value] = minimum coins needed to build `value`.
        for coin in usable_coins:
            # Iterate forward so the same coin can be reused multiple times.
            for value in range(coin, amount + 1):
                candidate = dp[value - coin] + 1
                if candidate < dp[value]:
                    dp[value] = candidate

        # If the sentinel remains, no combination can form the target amount.
        return dp[amount] if dp[amount] != unreachable else -1