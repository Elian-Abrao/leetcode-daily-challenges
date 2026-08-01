from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Sort cuts to enable interval DP; add boundaries 0 and n
        cuts = sorted([0] + cuts + [n])
        m = len(cuts)
        
        # dp[i][j] = minimum cost to make all cuts between cuts[i] and cuts[j]
        # where i and j are indices in the extended cuts array
        dp = [[0] * m for _ in range(m)]
        
        # Iterate over all possible segment lengths (gap between i and j)
        # We solve smaller subproblems first (bottom-up DP)
        for length in range(2, m):  # length = j - i
            for i in range(m - length):
                j = i + length
                dp[i][j] = float('inf')
                
                # Try making each cut k between i and j as the last cut
                # Cost = length of current stick + cost of left part + cost of right part
                for k in range(i + 1, j):
                    # Current stick goes from cuts[i] to cuts[j]
                    stick_length = cuts[j] - cuts[i]
                    # Cost if we make cut at position cuts[k] last
                    cost = stick_length + dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j], cost)
        
        # Answer: minimum cost to cut the entire stick from 0 to n
        return dp[0][m - 1]