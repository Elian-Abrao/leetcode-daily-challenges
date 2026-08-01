from typing import List

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        
        # Step 1: Find the bounding rectangle for each color
        colors = set()
        for row in targetGrid:
            colors.update(row)
        
        bounds = {}
        for color in colors:
            min_r, max_r = m, -1
            min_c, max_c = n, -1
            for r in range(m):
                for c in range(n):
                    if targetGrid[r][c] == color:
                        min_r = min(min_r, r)
                        max_r = max(max_r, r)
                        min_c = min(min_c, c)
                        max_c = max(max_c, c)
            bounds[color] = (min_r, max_r, min_c, max_c)
        
        # Step 2: Build dependency graph
        graph = {color: set() for color in colors}
        
        for color in colors:
            min_r, max_r, min_c, max_c = bounds[color]
            for r in range(min_r, max_r + 1):
                for c in range(min_c, max_c + 1):
                    other = targetGrid[r][c]
                    if other != color:
                        graph[other].add(color)
        
        # Step 3: Topological sort using DFS with cycle detection
        state = {color: 0 for color in colors}
        
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            
            state[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2
            return True
        
        for color in colors:
            if state[color] == 0:
                if not dfs(color):
                    return False
        
        return True