from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Edge case: if the grid is too small, no water can be trapped
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        
        # If either dimension is <= 2, water cannot be trapped
        if m <= 2 or n <= 2:
            return 0
        
        # Min heap to process cells from lowest to highest boundary
        # Each element: (height, row, col)
        min_heap = []
        
        # Track visited cells to avoid reprocessing
        visited = [[False] * n for _ in range(m)]
        
        # Initialize heap with all boundary cells
        # Water level is constrained by the boundaries (like a container)
        for i in range(m):
            for j in range(n):
                # Add all border cells to heap
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        total_water = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Process cells from lowest boundary inward
        # Key insight: water level at any cell is determined by the minimum
        # boundary height that surrounds it
        while min_heap:
            height, row, col = heapq.heappop(min_heap)
            
            # Explore all 4 neighbors
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                # Skip if out of bounds or already visited
                if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                    continue
                
                # Mark as visited
                visited[nr][nc] = True
                
                # Water can be trapped if current boundary height > neighbor height
                # The water level at this cell is at least 'height' (current boundary)
                if height > heightMap[nr][nc]:
                    total_water += height - heightMap[nr][nc]
                
                # Add neighbor to heap with effective height
                # Effective height is max of cell's own height and current water level
                # This ensures water level never decreases as we move inward
                heapq.heappush(min_heap, (max(height, heightMap[nr][nc]), nr, nc))
        
        return total_water