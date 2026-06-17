from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # The matrix can be treated as a sorted 1D array due to the properties:
        # - Each row is sorted
        # - First element of row i+1 > last element of row i
        # This allows us to perform binary search in O(log(m*n)) time
        
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)  # number of rows
        n = len(matrix[0])  # number of columns
        
        # Binary search treating the 2D matrix as a 1D sorted array
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Convert 1D index to 2D coordinates
            # row = mid // n, col = mid % n
            mid_value = matrix[mid // n][mid % n]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                # Target is in the right half
                left = mid + 1
            else:
                # Target is in the left half
                right = mid - 1
        
        # Target not found
        return False