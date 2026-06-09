from typing import List
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Edge case: if we have 1 or 2 points, all lie on the same line
        if len(points) <= 2:
            return len(points)
        
        max_points = 0
        
        # For each point, treat it as an anchor and count lines through it
        for i in range(len(points)):
            # Map from slope to count of points sharing that slope with anchor point i
            slope_count = {}
            
            # Compare anchor point i with all subsequent points
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                # Normalize the slope to avoid floating point precision issues
                # We represent slope as (dy/dx) but store as reduced fraction (dy, dx)
                # Handle vertical lines (dx == 0) separately by keeping dx = 0
                if dx == 0:
                    # Vertical line: all points have same x-coordinate
                    slope_key = (1, 0)  # Represents infinite slope
                elif dy == 0:
                    # Horizontal line: all points have same y-coordinate
                    slope_key = (0, 1)  # Represents zero slope
                else:
                    # Reduce the fraction dy/dx to its simplest form using GCD
                    # This ensures that slopes like 2/4 and 1/2 map to the same key
                    g = gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g
                    
                    # Normalize sign: keep dx positive to ensure consistency
                    # E.g., (-2, -3) and (2, 3) represent the same slope
                    if dx < 0:
                        dx, dy = -dx, -dy
                    
                    slope_key = (dy, dx)
                
                # Increment count for this slope
                slope_count[slope_key] = slope_count.get(slope_key, 0) + 1
            
            # The maximum count for any slope through point i, plus point i itself
            if slope_count:
                max_on_line = max(slope_count.values()) + 1
                max_points = max(max_points, max_on_line)
        
        return max_points