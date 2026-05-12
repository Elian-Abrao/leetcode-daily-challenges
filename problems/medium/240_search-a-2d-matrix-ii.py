from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Edge case: empty matrix
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        # Start from top-right corner (or could start from bottom-left)
        # This position allows us to eliminate either a row or column each step
        row, col = 0, n - 1
        
        # Key insight: at top-right corner:
        # - Moving left decreases values (since rows are sorted)
        # - Moving down increases values (since columns are sorted)
        # This gives us a clear decision path at each step
        
        while row < m and col >= 0:
            current = matrix[row][col]
            
            if current == target:
                # Found the target
                return True
            elif current > target:
                # Current value too large, eliminate this column
                # Move left to potentially smaller values
                col -= 1
            else:
                # Current value too small, eliminate this row
                # Move down to potentially larger values
                row += 1
        
        # Target not found after exhausting search space
        return False
        
        # Time Complexity: O(m + n) - worst case we traverse from top-right to bottom-left
        # Space Complexity: O(1) - only using constant extra space