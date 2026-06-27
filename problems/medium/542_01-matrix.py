from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Multi-source BFS approach: treat all 0s as starting points
        # and propagate distances outward level by level
        
        m, n = len(mat), len(mat[0])
        
        # Initialize result matrix with -1 (unvisited marker)
        result = [[-1] * n for _ in range(m)]
        
        # Queue for BFS: stores (row, col) tuples
        queue = deque()
        
        # Enqueue all cells with 0 and mark them as distance 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
        
        # Four directional neighbors: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # BFS to compute shortest distance from any 0
        while queue:
            row, col = queue.popleft()
            current_dist = result[row][col]
            
            # Explore all 4 neighbors
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds
                if 0 <= new_row < m and 0 <= new_col < n:
                    # If cell hasn't been visited yet (-1), update distance
                    if result[new_row][new_col] == -1:
                        result[new_row][new_col] = current_dist + 1
                        queue.append((new_row, new_col))
        
        return result