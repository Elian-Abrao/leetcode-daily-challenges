from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # Key insight: A perfect rectangle cover must satisfy two conditions:
        # 1. The sum of all small rectangle areas equals the large rectangle area
        # 2. All interior corners must appear an even number of times (2 or 4),
        #    and exactly 4 corners (the outer corners) appear once each
        
        # Track the bounding box of the perfect rectangle
        min_x = float('inf')
        min_y = float('inf')
        max_a = float('-inf')
        max_b = float('-inf')
        
        # Sum of all individual rectangle areas
        total_area = 0
        
        # Track all corners: a corner appearing odd times will remain in set
        # A corner appearing even times will be added/removed and not remain
        corners = set()
        
        for x, y, a, b in rectangles:
            # Update bounding box
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            
            # Add area of current rectangle
            total_area += (a - x) * (b - y)
            
            # Each rectangle contributes 4 corners
            # If a corner appears even times (2 or 4), it's an interior point
            # If it appears odd times (1 or 3), it should be an outer corner
            # Using XOR logic with set: toggle presence
            four_corners = [(x, y), (x, b), (a, y), (a, b)]
            for corner in four_corners:
                if corner in corners:
                    corners.remove(corner)  # Even occurrence
                else:
                    corners.add(corner)  # Odd occurrence
        
        # Calculate expected area of the bounding rectangle
        expected_area = (max_a - min_x) * (max_b - min_y)
        
        # Condition 1: Areas must match (no gaps, no overlaps)
        if total_area != expected_area:
            return False
        
        # Condition 2: Exactly 4 corners should appear odd times (the outer corners)
        if len(corners) != 4:
            return False
        
        # Verify the 4 remaining corners are exactly the bounding box corners
        expected_corners = {(min_x, min_y), (min_x, max_b), (max_a, min_y), (max_a, max_b)}
        if corners != expected_corners:
            return False
        
        return True