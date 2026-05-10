from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Create a list of (start, original_index) tuples
        # We need to track original indices since we'll be sorting
        starts = [(interval[0], i) for i, interval in enumerate(intervals)]
        
        # Sort by start time for efficient binary search
        # Time: O(n log n)
        starts.sort()
        
        # Extract just the start values for binary search
        start_values = [s[0] for s in starts]
        
        result = []
        
        # For each interval, find the right interval
        for interval in intervals:
            end = interval[1]
            
            # Binary search for the smallest start >= end
            # bisect_left finds the leftmost position where end can be inserted
            # to keep the list sorted, which gives us the smallest start >= end
            pos = bisect.bisect_left(start_values, end)
            
            # If pos is out of bounds, no right interval exists
            if pos >= len(starts):
                result.append(-1)
            else:
                # The interval at position pos has start >= end
                # Return its original index
                result.append(starts[pos][1])
        
        return result