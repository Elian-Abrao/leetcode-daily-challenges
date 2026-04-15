from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        # Helper: number of elements <= x using a staircase search
        def count_le(x: int) -> int:
            count = 0
            row = n - 1  # start from bottom-left
            col = 0
            # Move up when current element > x, else move right
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    # All elements in this column up to 'row' are <= x
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        lo, hi = matrix[0][0], matrix[-1][-1]
        # Binary search on value domain for the k-th smallest
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo