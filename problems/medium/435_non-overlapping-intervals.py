from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Edge case: empty or single interval - no removal needed
        if len(intervals) <= 1:
            return 0
        
        # Sort intervals by end time (greedy approach)
        # Choosing intervals that end earliest allows maximum room for future intervals
        intervals.sort(key=lambda x: x[1])
        
        # Track the end time of the last kept interval
        last_end = intervals[0][1]
        
        # Count how many intervals we can keep (non-overlapping)
        keep_count = 1
        
        # Iterate through sorted intervals starting from second
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            # If current interval doesn't overlap with last kept interval
            # (touching at a point is considered non-overlapping: start >= last_end)
            if start >= last_end:
                # Keep this interval
                keep_count += 1
                last_end = end
            # else: current interval overlaps, so we "remove" it (don't update last_end)
        
        # Minimum removals = total intervals - maximum non-overlapping intervals we can keep
        return len(intervals) - keep_count