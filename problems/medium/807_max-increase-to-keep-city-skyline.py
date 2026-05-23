from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Compute the maximum height in each row (viewed from east/west)
        # This represents the skyline constraint from the sides
        row_max = [max(grid[r]) for r in range(n)]
        
        # Compute the maximum height in each column (viewed from north/south)
        # This represents the skyline constraint from the top/bottom
        col_max = [max(grid[r][c] for r in range(n)) for c in range(n)]
        
        # The maximum height a building at (r, c) can reach is the minimum
        # of the row and column skyline constraints. This ensures that:
        # - It doesn't exceed the row's max (preserving east/west skyline)
        # - It doesn't exceed the column's max (preserving north/south skyline)
        total_increase = 0
        for r in range(n):
            for c in range(n):
                # Max allowable height is constrained by both skylines
                max_height = min(row_max[r], col_max[c])
                # Add the increase from current height to max allowable
                total_increase += max_height - grid[r][c]
        
        return total_increase