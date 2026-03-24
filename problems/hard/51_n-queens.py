from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Constraint guarantees n >= 1, but keeping the empty case makes the method robust.
        if n <= 0:
            return []

        results: List[List[str]] = []

        # Track which columns and diagonals are already occupied by earlier rows.
        # This lets each placement check run in O(1).
        used_columns = set()
        used_diag_main = set()   # row - col
        used_diag_anti = set()   # row + col

        # queens[row] = chosen column for that row.
        # Building by row guarantees at most one queen per row automatically.
        queens = [-1] * n

        def build_board() -> List[str]:
            # Convert the compact column representation into the required board strings.
            board = []
            for row in range(n):
                col = queens[row]
                board.append("." * col + "Q" + "." * (n - col - 1))
            return board

        def backtrack(row: int) -> None:
            # Reaching row n means all rows are filled with a valid non-attacking layout.
            if row == n:
                results.append(build_board())
                return

            for col in range(n):
                diag_main = row - col
                diag_anti = row + col

                # A queen attacks along its column and both diagonals.
                if (
                    col in used_columns
                    or diag_main in used_diag_main
                    or diag_anti in used_diag_anti
                ):
                    continue

                # Place the queen and reserve all attacked lines for deeper recursion.
                queens[row] = col
                used_columns.add(col)
                used_diag_main.add(diag_main)
                used_diag_anti.add(diag_anti)

                backtrack(row + 1)

                # Undo the placement so other columns in this row can be explored.
                used_columns.remove(col)
                used_diag_main.remove(diag_main)
                used_diag_anti.remove(diag_anti)
                queens[row] = -1

        backtrack(0)
        return results