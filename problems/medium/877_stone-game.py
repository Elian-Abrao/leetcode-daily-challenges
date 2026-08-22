from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        Returns True if Alice can win the Stone Game given optimal play.
        Uses DP to compute the maximum net advantage (current player score minus
        opponent score) for any subarray [i, j].
        """
        n = len(piles)
        # dp[i][j] = net advantage for the player whose turn it is
        # when the remaining subarray is piles[i..j] inclusive.
        dp = [[0] * n for _ in range(n)]

        # Base: single pile -> the player takes it, advantage = piles[i]
        for i in range(n):
            dp[i][i] = piles[i]

        # Fill DP for increasing lengths (len = j - i + 1)
        # The order of loops ensures that subproblems of smaller length
        # are already solved.
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # Two choices: take left or right.
                # After taking piles[i], opponent gets dp[i+1][j] advantage.
                # So net advantage = piles[i] - dp[i+1][j].
                # Similarly for piles[j].
                left = piles[i] - dp[i + 1][j]
                right = piles[j] - dp[i][j - 1]
                dp[i][j] = max(left, right)

        # Alice wins if her net advantage over the entire array is positive.
        return dp[0][n - 1] > 0