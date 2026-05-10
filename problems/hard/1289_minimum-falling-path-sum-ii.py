from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Edge case: single cell grid
        if n == 1:
            return grid[0][0]
        
        # dp[j] represents the minimum falling path sum ending at column j in the current row
        # We use rolling array to optimize space from O(n^2) to O(n)
        dp = grid[0][:]
        
        # Process each row starting from row 1
        for i in range(1, n):
            # For optimal O(n^2) solution, we need to find the two smallest values from previous row
            # This allows us to avoid O(n^3) by not checking all columns for each cell
            
            # Find the minimum and second minimum values and their indices from previous row
            min1_val = float('inf')
            min1_idx = -1
            min2_val = float('inf')
            
            for j in range(n):
                if dp[j] < min1_val:
                    # New global minimum found, shift old minimum to second place
                    min2_val = min1_val
                    min1_val = dp[j]
                    min1_idx = j
                elif dp[j] < min2_val:
                    # New second minimum found
                    min2_val = dp[j]
            
            # Build new dp array for current row
            new_dp = [0] * n
            for j in range(n):
                # If current column j is not the column with minimum from previous row,
                # we can use min1_val; otherwise we must use min2_val to satisfy non-zero shift
                if j != min1_idx:
                    new_dp[j] = grid[i][j] + min1_val
                else:
                    new_dp[j] = grid[i][j] + min2_val
            
            dp = new_dp
        
        # Return the minimum value from the last row
        return min(dp)