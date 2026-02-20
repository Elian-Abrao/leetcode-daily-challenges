from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        res: List[int] = []
        for k in range(m + n - 1):
            if k % 2 == 0:
                i = min(k, m - 1)
                j = k - i
                while i >= 0 and j < n:
                    res.append(mat[i][j])
                    i -= 1
                    j += 1
            else:
                j = min(k, n - 1)
                i = k - j
                while j >= 0 and i < m:
                    res.append(mat[i][j])
                    i += 1
                    j -= 1
        return res