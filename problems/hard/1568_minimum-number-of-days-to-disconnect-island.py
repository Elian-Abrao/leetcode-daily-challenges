from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def count_islands():
            """Count the number of islands using DFS."""
            visited = [[False] * n for _ in range(m)]
            
            def dfs(i, j):
                if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == 0:
                    return
                visited[i][j] = True
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
            
            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        dfs(i, j)
                        islands += 1
            return islands
        
        # Edge case: already disconnected or no island
        initial_islands = count_islands()
        if initial_islands != 1:
            return 0
        
        # Try removing each land cell and check if it disconnects the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # Temporarily remove this land cell
                    grid[i][j] = 0
                    
                    # Check if grid is now disconnected
                    if count_islands() != 1:
                        grid[i][j] = 1  # Restore
                        return 1
                    
                    # Restore the cell
                    grid[i][j] = 1
        
        # If no single removal works, we need at most 2 days
        return 2