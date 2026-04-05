from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Constraints guarantee at least one cell, but keeping the guard makes
        # the method robust and documents the expected empty-input behavior.
        if not mat or not mat[0]:
            return []

        rows = len(mat)
        cols = len(mat[0])
        total = rows * cols
        result = [0] * total

        row = 0
        col = 0
        direction = 1  # 1 means up-right, -1 means down-left.

        for index in range(total):
            # Record the current cell before deciding how to move next.
            result[index] = mat[row][col]

            if direction == 1:
                # When moving up-right, hitting the last column forces us down.
                if col == cols - 1:
                    row += 1
                    direction = -1
                # Hitting the top row forces us right.
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    # Inside bounds, keep following the current diagonal.
                    row -= 1
                    col += 1
            else:
                # When moving down-left, hitting the last row forces us right.
                if row == rows - 1:
                    col += 1
                    direction = 1
                # Hitting the first column forces us down.
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    # Inside bounds, keep following the current diagonal.
                    row += 1
                    col -= 1

        return result