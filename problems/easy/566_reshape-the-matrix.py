from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
        
        reshaped = [[0] * c for _ in range(r)]
        
        for i in range(m):
            for j in range(n):
                flat_index = i * n + j
                new_row = flat_index // c
                new_col = flat_index % c
                reshaped[new_row][new_col] = mat[i][j]
        
        return reshaped