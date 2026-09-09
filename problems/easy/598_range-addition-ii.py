from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """
        After performing all operations, the maximum value will be in the region
        that receives the most increments. Since each operation increments a
        contiguous submatrix starting at (0,0), the maximum value appears in the
        intersection of all these submatrices. That intersection's size is
        the smallest ai times the smallest bi.
        """
        # If there are no operations, the whole matrix is zeros, so all cells
        # are the "maximum" (value 0). Return total cell count.
        if not ops:
            return m * n

        # Track the minimum ai and bi across all operations.
        # These define the top-left rectangle that every operation covers.
        min_a = m  # Initially max possible, will shrink
        min_b = n

        for a, b in ops:
            # Clamp to valid ranges (ai <= m, bi <= n per constraints)
            if a < min_a:
                min_a = a
            if b < min_b:
                min_b = b
            # Early exit: if both are already 1, cannot shrink further
            if min_a == 1 and min_b == 1:
                return 1

        # The number of cells that receive the maximum increment
        return min_a * min_b