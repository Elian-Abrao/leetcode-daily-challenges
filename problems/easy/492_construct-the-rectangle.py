from typing import List
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Start from the square root of area and search downward
        # The largest divisor <= sqrt(area) will minimize L - W
        w = int(math.sqrt(area))
        
        # Find the largest W that divides area evenly, starting from sqrt(area)
        while w > 0:
            if area % w == 0:
                # Found a valid width
                l = area // w
                return [l, w]
            w -= 1
        
        # This should never be reached given constraints (area >= 1)
        # but logically, area = area * 1 is always valid
        return [area, 1]