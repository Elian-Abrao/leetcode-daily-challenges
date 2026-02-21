from __future__ import annotations

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # Normalize so n <= m to reduce symmetric states
        if n > m:
            n, m = m, n

        self.n, self.m = n, m
        # Grid representation: False = empty, True = filled
        self.grid = [[False] * m for _ in range(n)]
        # Upper bound: fill with 1x1 squares (worst case)
        self.best = n * m

        self._dfs(0)
        return self.best

    def _dfs(self, count: int) -> None:
        # Prune if we already used as many squares as the best found
        if count >= self.best:
            return

        n, m = self.n, self.m

        # Find the first empty cell (top-left most)
        start_i = start_j = -1
        found = False
        for i in range(n):
            row = self.grid[i]
            for j in range(m):
                if not row[j]:
                    start_i, start_j = i, j
                    found = True
                    break
            if found:
                break

        # If no empty cell found, we tiled the rectangle
        if not found:
            self.best = count
            return

        # At position (start_i, start_j), try to place the largest possible square first
        max_side = min(n - start_i, m - start_j)

        for s in range(max_side, 0, -1):
            # Check if s x s area is all empty
            ok = True
            for r in range(start_i, start_i + s):
                row = self.grid[r]
                for c in range(start_j, start_j + s):
                    if row[c]:
                        ok = False
                        break
                if not ok:
                    break

            if not ok:
                continue  # Try smaller square

            # Place the square by marking cells as filled
            for r in range(start_i, start_i + s):
                for c in range(start_j, start_j + s):
                    self.grid[r][c] = True

            # Recurse with one more square used
            self._dfs(count + 1)

            # Backtrack: unplace the square
            for r in range(start_i, start_i + s):
                for c in range(start_j, start_j + s):
                    self.grid[r][c] = False