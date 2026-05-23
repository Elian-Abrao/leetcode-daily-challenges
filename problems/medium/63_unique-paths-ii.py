from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Edge case: if start or end is blocked, no path exists
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Use a 1D DP array to save space (rolling array technique)
        # dp[j] represents the number of ways to reach column j in the current row
        dp = [0] * n
        dp[0] = 1  # Starting position
        
        # Process each cell row by row
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    # Cell is blocked, no paths through here
                    dp[j] = 0
                elif j > 0:
                    # Current cell can be reached from left (dp[j-1]) or top (dp[j])
                    # dp[j] still contains the value from the previous row (top)
                    # dp[j-1] contains the value from the current row (left)
                    dp[j] += dp[j - 1]
                # else: j == 0, dp[0] keeps its value from above (unless blocked)
        
        return dp[n - 1]