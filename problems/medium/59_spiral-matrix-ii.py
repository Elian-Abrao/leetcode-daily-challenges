from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Boundary pointers for the current layer
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        # Current number to fill
        num = 1
        
        # Process layer by layer until all cells are filled
        while top <= bottom and left <= right:
            # Fill top row (left to right)
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1  # Move top boundary down
            
            # Fill right column (top to bottom)
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1  # Move right boundary left
            
            # Fill bottom row (right to left)
            # Check if there's still a bottom row to fill
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1  # Move bottom boundary up
            
            # Fill left column (bottom to top)
            # Check if there's still a left column to fill
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1  # Move left boundary right
        
        return matrix