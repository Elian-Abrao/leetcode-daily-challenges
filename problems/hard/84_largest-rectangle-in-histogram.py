from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Use a monotonic increasing stack to track indices of bars
        # Key insight: for each bar, we want to find the maximum width
        # rectangle that can be formed with that bar as the shortest height
        
        stack = []  # Stack stores indices of bars in increasing height order
        max_area = 0
        
        for i, h in enumerate(heights):
            # When we encounter a bar shorter than stack top,
            # we can calculate areas for all taller bars in stack
            # because current bar limits their right extension
            while stack and heights[stack[-1]] > h:
                # Pop the tallest bar that can't extend further right
                height_idx = stack.pop()
                height = heights[height_idx]
                
                # Width calculation:
                # - Right boundary: current index i (exclusive)
                # - Left boundary: index after the new stack top (exclusive)
                # - If stack empty, the popped bar extends all the way to left (index 0)
                width = i if not stack else i - stack[-1] - 1
                
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        # Process remaining bars in stack
        # These bars can extend all the way to the right end
        while stack:
            height_idx = stack.pop()
            height = heights[height_idx]
            
            # Width extends to the end of array
            # Left boundary is determined by remaining stack top
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            
            max_area = max(max_area, height * width)
        
        return max_area