from __future__ import annotations

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n_rows = len(matrix)
        if n_rows == 0:
            return 0
        n_cols = len(matrix[0])
        prev = matrix[0][:]  # copy first row

        for r in range(1, n_rows):
            cur = [0] * n_cols
            for c in range(n_cols):
                top_left = prev[c - 1] if c > 0 else float('inf')
                top_mid = prev[c]
                top_right = prev[c + 1] if c < n_cols - 1 else float('inf')
                best = min(top_left, top_mid, top_right)
                cur[c] = matrix[r][c] + best
            prev = cur

        return min(prev)