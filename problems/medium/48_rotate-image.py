from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Step 1: Transpose the matrix (swap across main diagonal)
        # Only need to iterate over upper triangle to avoid double-swapping
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row to complete the 90-degree clockwise rotation
        for i in range(n):
            matrix[i].reverse()