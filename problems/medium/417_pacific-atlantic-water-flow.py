from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # Track cells that can reach each ocean
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, reachable, prev_height):
            # Skip if out of bounds, already visited, or water can't flow here
            # (water flows to cells with equal or lower height, so we traverse backwards
            # from ocean: only go to cells with equal or higher height)
            if (r < 0 or r >= m or c < 0 or c >= n or 
                (r, c) in reachable or 
                heights[r][c] < prev_height):
                return
            
            reachable.add((r, c))
            
            # Explore all 4 directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(r + dr, c + dc, reachable, heights[r][c])
        
        # Start DFS from all Pacific border cells (top row and left column)
        for c in range(n):
            dfs(0, c, pacific_reachable, heights[0][c])
        for r in range(m):
            dfs(r, 0, pacific_reachable, heights[r][0])
        
        # Start DFS from all Atlantic border cells (bottom row and right column)
        for c in range(n):
            dfs(m - 1, c, atlantic_reachable, heights[m - 1][c])
        for r in range(m):
            dfs(r, n - 1, atlantic_reachable, heights[r][n - 1])
        
        # Find intersection: cells that can reach both oceans
        result = []
        for r, c in pacific_reachable:
            if (r, c) in atlantic_reachable:
                result.append([r, c])
        
        return result