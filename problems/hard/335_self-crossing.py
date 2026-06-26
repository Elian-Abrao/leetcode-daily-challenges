from typing import List

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        
        # Need at least 4 lines to have a crossing
        if n < 4:
            return False
        
        # Check each line starting from the 4th one
        for i in range(3, n):
            # Case 1: i-th line crosses (i-3)-th line
            # This happens when the spiral starts closing inward
            # Current line (going in same direction as i-3) is long enough 
            # and previous line is short enough
            if i >= 3:
                # Line i goes in same direction as line i-3
                # Line i-1 is perpendicular and goes "back"
                # Check if line i reaches or crosses line i-3
                if (distance[i] >= distance[i-2] and 
                    distance[i-1] <= distance[i-3]):
                    return True
            
            # Case 2: i-th line crosses (i-4)-th line
            # This is a more complex scenario where the 5th line crosses the 1st
            if i >= 4:
                # Line i and line i-4 are perpendicular
                # Line i-3 and line i-1 are parallel to each other, perpendicular to i and i-4
                # Check if line i can reach line i-4
                if (distance[i-1] == distance[i-3] and
                    distance[i] + distance[i-4] >= distance[i-2]):
                    return True
            
            # Case 3: i-th line crosses (i-5)-th line
            # Most complex case: 6th line crosses 1st line
            if i >= 5:
                # Multiple conditions need to be satisfied for this geometric configuration
                # Line i-2 must be shorter than i-4 (moving inward)
                # Line i-3 must be between i-5 and i-1 (specific positioning)
                # Line i must extend far enough to cross i-5
                if (distance[i-2] >= distance[i-4] and
                    distance[i-3] <= distance[i-1] and
                    distance[i-1] <= distance[i-3] + distance[i-5] and
                    distance[i-2] <= distance[i-4] + distance[i] and
                    distance[i] + distance[i-4] >= distance[i-2] and
                    distance[i-1] + distance[i-5] >= distance[i-3]):
                    return True
        
        return False