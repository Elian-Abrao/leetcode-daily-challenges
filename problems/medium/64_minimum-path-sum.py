from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Constraints guarantee at least one cell, but guarding keeps the method robust.
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        # dp[c] stores the minimum path sum to reach the current row at column c.
        # Using 1D DP reduces space from O(m * n) to O(n) while keeping O(m * n) time.
        dp = [0] * cols

        # Initialize the first cell separately because it has no predecessors.
        dp[0] = grid[0][0]

        # First row can only be reached from the left.
        for col in range(1, cols):
            dp[col] = dp[col - 1] + grid[0][col]

        # Process remaining rows.
        for row in range(1, rows):
            # First column can only be reached from above.
            dp[0] += grid[row][0]

            for col in range(1, cols):
                # The current cell is reachable either from above (old dp[col])
                # or from the left (updated dp[col - 1] in this row).
                dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]

        # Bottom-right cell's minimum path sum.
        return dp[-1]