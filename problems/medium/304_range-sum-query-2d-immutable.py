from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Edge case: empty matrix
        if not matrix or not matrix[0]:
            self.prefix = []
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # Build 2D prefix sum array with extra padding to avoid boundary checks
        # prefix[i][j] represents sum of all elements in rectangle from (0,0) to (i-1, j-1)
        # Adding 1 extra row and column (initialized to 0) simplifies boundary handling
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill prefix sum array using inclusion-exclusion principle
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Current cell value from original matrix
                # Add sum from top, left, subtract overlap (top-left), add current
                self.prefix[i][j] = (
                    matrix[i - 1][j - 1] +  # Current element
                    self.prefix[i - 1][j] +  # Sum from above
                    self.prefix[i][j - 1] -  # Sum from left
                    self.prefix[i - 1][j - 1]  # Subtract overlap (counted twice)
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Handle empty matrix edge case
        if not self.prefix:
            return 0
        
        # Use inclusion-exclusion to compute rectangle sum in O(1)
        # Sum of rectangle = total area - top strip - left strip + top-left corner
        # Shift indices by 1 due to padding in prefix array
        return (
            self.prefix[row2 + 1][col2 + 1] -  # Sum up to bottom-right
            self.prefix[row1][col2 + 1] -      # Subtract sum above the region
            self.prefix[row2 + 1][col1] +      # Subtract sum to the left of the region
            self.prefix[row1][col1]             # Add back the overlap (subtracted twice)
        )