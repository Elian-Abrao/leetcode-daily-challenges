class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Dynamic Programming approach with space optimization
        # Key insight: paths to cell (i,j) = paths to (i-1,j) + paths to (i,j-1)
        # We only need the previous row to compute the current row
        
        # Edge case: single row or single column grid
        if m == 1 or n == 1:
            return 1
        
        # Use a 1D array to store the number of paths for each column
        # dp[j] represents the number of ways to reach current row, column j
        dp = [1] * n  # Initialize first row: all cells have 1 path (move right only)
        
        # Process each row starting from the second row
        for i in range(1, m):
            # For each column in the current row
            for j in range(1, n):
                # Current cell paths = paths from above (dp[j]) + paths from left (dp[j-1])
                # dp[j] still holds the value from previous row (cell above)
                # dp[j-1] was just updated, so it holds current row's left neighbor
                dp[j] += dp[j - 1]
            
            # Note: dp[0] remains 1 for all rows (leftmost column has only 1 path)
        
        # The bottom-right corner result is stored in the last position
        return dp[n - 1]