from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Edge case: single interval or empty
        if len(intervals) <= 1:
            return intervals
        
        # Sort intervals by start time
        # This allows us to process in order and merge greedily
        # Time: O(n log n), Space: O(1) or O(n) depending on sort implementation
        intervals.sort(key=lambda x: x[0])
        
        # Result list to hold merged intervals
        merged = []
        
        # Initialize with the first interval
        current_start, current_end = intervals[0]
        
        # Iterate through sorted intervals starting from second
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            # Check if current interval overlaps with the accumulated interval
            # Overlapping condition: start <= current_end
            # (touching intervals like [1,4] and [4,5] are considered overlapping)
            if start <= current_end:
                # Merge by extending the end to the maximum of both ends
                current_end = max(current_end, end)
            else:
                # No overlap: save the current merged interval
                merged.append([current_start, current_end])
                # Start a new interval
                current_start, current_end = start, end
        
        # Don't forget to add the last accumulated interval
        merged.append([current_start, current_end])
        
        return merged