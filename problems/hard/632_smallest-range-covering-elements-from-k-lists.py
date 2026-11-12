from __future__ import annotations
import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        Finds the smallest range [a, b] such that at least one number from each
        of the k sorted lists is included in the range.

        Approach: min-heap with k pointers, sliding window on the heap values.
        """
        k = len(nums)
        # Each element in heap: (value, list_index, element_index)
        heap = []
        current_max = float('-inf')
        
        # Initialize heap with the first element from each list.
        # Track the global maximum among these first elements.
        for i in range(k):
            if nums[i]:  # ensure list is not empty per constraints
                val = nums[i][0]
                heapq.heappush(heap, (val, i, 0))
                current_max = max(current_max, val)
        
        # If any list is empty, the problem expects a valid range anyway,
        # but constraints guarantee at least one element per list.
        # Initialize answer with the widest possible range.
        best_left, best_right = float('-inf'), float('inf')
        
        # Main loop: pop the smallest element, update the range, then push next.
        while heap:
            min_val, list_idx, elem_idx = heapq.heappop(heap)
            
            # Update best range if current window is smaller.
            # Range comparison: first by length, then by left value.
            current_range = current_max - min_val
            best_range = best_right - best_left
            if current_range < best_range or (current_range == best_range and min_val < best_left):
                best_left, best_right = min_val, current_max
            
            # If this was the last element in its list, we cannot expand further
            # (every list must contribute, so we stop).
            if elem_idx + 1 == len(nums[list_idx]):
                break
            
            # Move pointer forward in this list: push the next element.
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            # Update the global maximum for the current window.
            current_max = max(current_max, next_val)
        
        return [best_left, best_right]