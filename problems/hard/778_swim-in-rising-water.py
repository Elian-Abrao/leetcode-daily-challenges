from __future__ import annotations
import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        Returns the minimum time t such that a path exists from (0,0) to (n-1,n-1)
        where every cell on the path has elevation <= t.
        Uses Dijkstra-like minimax approach with a min-heap.
        """
        n = len(grid)
        # distance[i][j] = minimal maximum elevation to reach (i, j)
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]

        # Min-heap entries: (current max elevation, row, col)
        heap = [(grid[0][0], 0, 0)]
        dist[0][0] = grid[0][0]

        # Directions: up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            cur_max, r, c = heapq.heappop(heap)

            # If we've already found a better path to this cell, skip
            if cur_max > dist[r][c]:
                continue

            # Early exit: reached target
            if r == n - 1 and c == n - 1:
                return cur_max

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    # The new max for this neighbor is max(cur_max, grid[nr][nc])
                    new_max = max(cur_max, grid[nr][nc])
                    if new_max < dist[nr][nc]:
                        dist[nr][nc] = new_max
                        heapq.heappush(heap, (new_max, nr, nc))

        # The target must be reachable (grid is connected with enough water)
        return dist[n - 1][n - 1]