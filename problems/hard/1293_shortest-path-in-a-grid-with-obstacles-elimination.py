from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # Edge case: if k is large enough, we can eliminate all obstacles
        # and the shortest path is just the Manhattan distance
        if k >= m + n - 2:
            return m + n - 2
        
        # BFS with state: (row, col, obstacles_eliminated)
        # We want to find shortest path, so BFS is appropriate
        queue = deque([(0, 0, 0, 0)])  # (row, col, obstacles_used, steps)
        
        # visited[r][c] = minimum obstacles used to reach (r, c)
        # We only revisit a cell if we can reach it with fewer obstacles used
        visited = {}
        visited[(0, 0)] = 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            row, col, obstacles_used, steps = queue.popleft()
            
            # Check if we reached the destination
            if row == m - 1 and col == n - 1:
                return steps
            
            # Explore all 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds
                if 0 <= new_row < m and 0 <= new_col < n:
                    # Calculate new obstacles used
                    new_obstacles_used = obstacles_used + grid[new_row][new_col]
                    
                    # Only proceed if we haven't exceeded k obstacles
                    if new_obstacles_used <= k:
                        # Only visit if we haven't been here before with fewer/equal obstacles
                        # or this is the first time visiting this cell
                        if (new_row, new_col) not in visited or visited[(new_row, new_col)] > new_obstacles_used:
                            visited[(new_row, new_col)] = new_obstacles_used
                            queue.append((new_row, new_col, new_obstacles_used, steps + 1))
        
        # No path found
        return -1