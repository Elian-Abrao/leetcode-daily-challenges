from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # dp[r][c1][c2] = max cherries when robot1 is at (r, c1) and robot2 is at (r, c2)
        # Use rolling array optimization: only need current and next row
        # Initialize with -infinity to mark unreachable states
        prev = [[[-1] * cols for _ in range(cols)] for _ in range(2)]
        curr_idx = 0
        
        # Base case: both robots start at row 0
        # Robot 1 at (0, 0), Robot 2 at (0, cols-1)
        prev[curr_idx][0][cols - 1] = grid[0][0] + (grid[0][cols - 1] if cols > 1 else 0)
        
        # Process each row
        for r in range(rows - 1):
            next_idx = 1 - curr_idx
            
            # Reset next row state
            for c1 in range(cols):
                for c2 in range(cols):
                    prev[next_idx][c1][c2] = -1
            
            # Try all valid positions for both robots at current row
            for c1 in range(cols):
                for c2 in range(cols):
                    if prev[curr_idx][c1][c2] == -1:
                        continue
                    
                    current_cherries = prev[curr_idx][c1][c2]
                    
                    # Each robot can move to 3 possible columns: -1, 0, +1
                    for dc1 in [-1, 0, 1]:
                        nc1 = c1 + dc1
                        if nc1 < 0 or nc1 >= cols:
                            continue
                        
                        for dc2 in [-1, 0, 1]:
                            nc2 = c2 + dc2
                            if nc2 < 0 or nc2 >= cols:
                                continue
                            
                            # Calculate cherries picked at next position
                            # If both robots are at same cell, count cherries only once
                            cherries_at_next = grid[r + 1][nc1]
                            if nc1 != nc2:
                                cherries_at_next += grid[r + 1][nc2]
                            
                            # Update DP state for next row
                            prev[next_idx][nc1][nc2] = max(
                                prev[next_idx][nc1][nc2],
                                current_cherries + cherries_at_next
                            )
            
            curr_idx = next_idx
        
        # Find maximum cherries collected at the last row
        max_cherries = 0
        for c1 in range(cols):
            for c2 in range(cols):
                if prev[curr_idx][c1][c2] != -1:
                    max_cherries = max(max_cherries, prev[curr_idx][c1][c2])
        
        return max_cherries