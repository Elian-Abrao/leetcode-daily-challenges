from __future__ import annotations
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Edge-case: if grid is empty
        if not grid or not grid[0]:
            return 0

        n = len(grid)
        label = 2  # start labeling islands from 2 to avoid collision with 0/1
        sizes = {}  # map island label -> its area

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # First pass: identify all islands and compute their areas using iterative DFS
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area = 0
                    stack = [(r, c)]
                    grid[r][c] = label  # mark with island label
                    while stack:
                        x, y = stack.pop()
                        area += 1
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                                grid[nx][ny] = label
                                stack.append((nx, ny))
                    sizes[label] = area
                    label += 1

        # Base maximum is the largest existing island (in case we don't flip any 0)
        max_size = max(sizes.values()) if sizes else 0

        # Second pass: for every 0 cell, consider flipping to 1 and connecting neighboring islands
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()  # to avoid counting the same island multiple times
                    total = 1  # this flipped cell
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < n and 0 <= nc < n:
                            lbl = grid[nr][nc]
                            if lbl > 1 and lbl not in seen:
                                seen.add(lbl)
                                total += sizes[lbl]
                    if total > max_size:
                        max_size = total

        return max_size