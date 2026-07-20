from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Edge case: empty matrix
        if not matrix or not matrix[0]:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Build histogram heights for each row
        # heights[i] represents consecutive 1's ending at current row in column i
        heights = [0] * cols
        max_area = 0
        
        # Process each row, treating it as the base of a histogram
        for row in range(rows):
            # Update heights: increment if '1', reset to 0 if '0'
            for col in range(cols):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
            
            # Compute max rectangle in this histogram
            max_area = max(max_area, self._largestRectangleInHistogram(heights))
        
        return max_area
    
    def _largestRectangleInHistogram(self, heights: List[int]) -> int:
        # Use stack-based approach to find largest rectangle in histogram
        # Stack stores indices of bars in increasing height order
        stack = []
        max_area = 0
        
        for i, h in enumerate(heights):
            # When we encounter a shorter bar, calculate areas for taller bars
            # that can no longer extend to the right
            while stack and heights[stack[-1]] > h:
                # Pop the tallest bar that's taller than current
                height_idx = stack.pop()
                height = heights[height_idx]
                
                # Width: from the bar after last smaller bar to current position
                # If stack is empty, this height extends from beginning
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        # Process remaining bars in stack
        # These bars can extend to the end of the histogram
        while stack:
            height_idx = stack.pop()
            height = heights[height_idx]
            # Width extends to the end of array
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area