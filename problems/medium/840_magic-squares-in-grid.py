from __future__ import annotations

class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # A 3x3 magic square is impossible if the grid is smaller than 3x3
        if rows < 3 or cols < 3:
            return 0

        # Predefine the target sum for a row/column/diagonal in a 3x3 magic square
        TARGET = 15

        # Check if the 3x3 subgrid starting at (r, c) forms a valid magic square
        def is_magic(r: int, c: int) -> bool:
            # Collect the 9 numbers in a set to verify distinctness and range 1..9
            seen = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    val = grid[i][j]
                    if val < 1 or val > 9:
                        return False
                    seen.add(val)
            if len(seen) != 9:
                return False

            # Row sums
            if grid[r][c] + grid[r][c+1] + grid[r][c+2] != TARGET:
                return False
            if grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != TARGET:
                return False
            if grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != TARGET:
                return False

            # Column sums
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != TARGET:
                return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != TARGET:
                return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != TARGET:
                return False

            # Diagonal sums
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != TARGET:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != TARGET:
                return False

            return True

        count = 0
        # Enumerate all possible top‑left corners of 3x3 subgrids
        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_magic(i, j):
                    count += 1
        return count