from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        0-1 knapsack on two dimensions: count of '0's up to m and count of '1's up to n.
        Each string is an item with weight (zeros, ones) and value 1.
        We maximize the number of strings chosen without exceeding m zeros and n ones.
        """
        # Precompute (zeros, ones) for each string
        counts = []
        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros
            counts.append((zeros, ones))

        # Initialize DP table with zeros: dp[i][j] = max number of strings using i zeros and j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Process each string as an item in 0-1 knapsack fashion
        for zeros, ones in counts:
            # Prune items that individually exceed capacity
            if zeros > m or ones > n:
                continue
            for i in range(m, zeros - 1, -1):
                # Local reference for speed is not strictly necessary here; kept simple
                for j in range(n, ones - 1, -1):
                    # Choose to take this string or not
                    candidate = dp[i - zeros][j - ones] + 1
                    if candidate > dp[i][j]:
                        dp[i][j] = candidate

        return dp[m][n]