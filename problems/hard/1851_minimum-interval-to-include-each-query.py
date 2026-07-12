from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by start position to process them left-to-right
        intervals.sort()
        
        # Create a list of (query_value, original_index) and sort by query_value
        # This allows us to process queries in increasing order while tracking original positions
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        # Result array to store answers in original query order
        result = [-1] * len(queries)
        
        # Min-heap to track active intervals by (size, end_position)
        # We use size as the first element to always get the smallest interval
        min_heap = []
        
        # Index to track which intervals we've already considered
        interval_idx = 0
        
        # Process each query in sorted order
        for query_val, original_idx in sorted_queries:
            # Add all intervals that start at or before current query
            while interval_idx < len(intervals) and intervals[interval_idx][0] <= query_val:
                left, right = intervals[interval_idx]
                size = right - left + 1
                # Push (size, right) so we can find minimum size interval
                heapq.heappush(min_heap, (size, right))
                interval_idx += 1
            
            # Remove intervals from heap that end before current query
            # These intervals don't contain the current query point
            while min_heap and min_heap[0][1] < query_val:
                heapq.heappop(min_heap)
            
            # If heap is not empty, the top element is the smallest valid interval
            if min_heap:
                result[original_idx] = min_heap[0][0]
        
        return result