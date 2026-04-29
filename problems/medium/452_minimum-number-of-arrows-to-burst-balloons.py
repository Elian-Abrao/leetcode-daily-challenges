from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Edge case: empty input (though constraints guarantee at least 1)
        if not points:
            return 0
        
        # Sort balloons by their end coordinate
        # This greedy choice allows us to shoot as late as possible,
        # maximizing the chance of hitting future overlapping balloons
        points.sort(key=lambda x: x[1])
        
        # Start with one arrow needed for the first balloon
        arrows = 1
        
        # Track the position where the current arrow is shot
        # We shoot at the end of the first balloon to maximize coverage
        current_arrow_pos = points[0][1]
        
        # Iterate through remaining balloons
        for i in range(1, len(points)):
            start, end = points[i]
            
            # If current balloon starts after the last arrow position,
            # we need a new arrow
            if start > current_arrow_pos:
                arrows += 1
                # Shoot the new arrow at the end of this balloon
                current_arrow_pos = end
            # Otherwise, the current arrow already bursts this balloon
            # (since current_arrow_pos <= end by our sort order,
            #  and start <= current_arrow_pos)
        
        return arrows