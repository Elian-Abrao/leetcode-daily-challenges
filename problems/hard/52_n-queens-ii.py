from __future__ import annotations

class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Count all distinct solutions for the N-Queens puzzle using bitmask backtracking.
        We place one queen per row. We track which columns, and both diagonals are under attack
        using bit masks. At each row, compute all safe positions, and try placing a queen
        in each safe spot, updating masks for the next row.
        """
        if n <= 0:
            return 0

        all_mask = (1 << n) - 1  # bits representing all columns in current board size
        count = 0

        def dfs(row: int, cols: int, diag1: int, diag2: int) -> None:
            nonlocal count
            if row == n:
                # All rows processed; found a valid arrangement
                count += 1
                return

            # Positions in this row that are not under attack by existing queens
            # available = all_mask & ~(cols | diag1 | diag2)
            available = (~(cols | diag1 | diag2)) & all_mask

            # Try each available position (LSB method to iterate bits)
            while available:
                bit = available & -available  # lowest set bit -> place queen here
                available -= bit

                # Place queen at 'bit' in current row, update masks for next row:
                # - cols: mark this column as occupied
                # - diag1: diagonals attacking next row when shifted left
                # - diag2: diagonals attacking next row when shifted right
                dfs(row + 1, cols | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1)

        dfs(0, 0, 0, 0)
        return count