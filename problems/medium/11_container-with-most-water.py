from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two-pointer approach: start from widest container and move inward
        # Key insight: moving the pointer with smaller height might find a taller line
        # that compensates for the reduced width
        
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area: width * min(left_height, right_height)
            # Water level is limited by the shorter line
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Track maximum area seen so far
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            # Rationale: keeping the taller line gives us better potential
            # for finding a larger area as we search inward
            if height[left] < height[right]:
                left += 1
            else:
                # Move right pointer even if heights are equal
                # (either choice works when equal)
                right -= 1
        
        return max_area