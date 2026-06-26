from typing import List
import bisect

class SummaryRanges:

    def __init__(self):
        # Store intervals as sorted list of [start, end]
        # Invariant: intervals are disjoint and sorted by start
        self.intervals = []

    def addNum(self, value: int) -> None:
        # Edge case: empty intervals list
        if not self.intervals:
            self.intervals.append([value, value])
            return
        
        # Find insertion position using binary search on interval starts
        # bisect_left gives us the position where value would be inserted
        pos = bisect.bisect_left(self.intervals, [value, value])
        
        # Check if value already covered by existing intervals
        # Need to check interval before pos (if exists) since it might contain value
        if pos > 0 and self.intervals[pos - 1][1] >= value:
            return  # Already in an interval
        
        # Check if value is in the interval at pos (if exists)
        if pos < len(self.intervals) and self.intervals[pos][0] <= value <= self.intervals[pos][1]:
            return  # Already in an interval
        
        # Determine merge candidates
        merge_left = False
        merge_right = False
        
        # Can we extend the interval to the left (interval before pos)?
        if pos > 0 and self.intervals[pos - 1][1] + 1 == value:
            merge_left = True
        
        # Can we extend the interval to the right (interval at pos)?
        if pos < len(self.intervals) and self.intervals[pos][0] - 1 == value:
            merge_right = True
        
        if merge_left and merge_right:
            # Merge both: extend left interval to cover right interval
            self.intervals[pos - 1][1] = self.intervals[pos][1]
            # Remove the right interval
            self.intervals.pop(pos)
        elif merge_left:
            # Extend left interval
            self.intervals[pos - 1][1] = value
        elif merge_right:
            # Extend right interval
            self.intervals[pos][0] = value
        else:
            # Create new interval at position pos
            self.intervals.insert(pos, [value, value])

    def getIntervals(self) -> List[List[int]]:
        # Return a copy to prevent external modification
        return self.intervals[:]