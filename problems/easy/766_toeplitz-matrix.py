from __future__ import annotations

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        """
        Returns True if the matrix is Toeplitz (every diagonal
        from top-left to bottom-right contains identical elements).
        """
        m = len(matrix)
        n = len(matrix[0])

        # Only need to check each element except the last row and last column.
        # If matrix[i][j] equals matrix[i+1][j+1], then the diagonal is consistent.
        for i in range(m - 1):
            for j in range(n - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False

        # All overlapping diagonals matched → matrix is Toeplitz.
        return True