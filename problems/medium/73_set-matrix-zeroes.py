from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Strategy: Use first row and first column as markers for which rows/cols to zero
        # Need separate flags for whether first row/col themselves should be zeroed
        
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # Track if first row and first column originally contain zeros
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Use first row and column as markers
        # Scan the interior of the matrix (excluding first row/col)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    # Mark the corresponding first row and first column cell
                    matrix[i][0] = 0  # Mark row i should be zeroed
                    matrix[0][j] = 0  # Mark column j should be zeroed
        
        # Zero out cells based on markers in first row and column
        # Process interior cells first to avoid interfering with markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Handle first row separately if it originally had a zero
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Handle first column separately if it originally had a zero
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0