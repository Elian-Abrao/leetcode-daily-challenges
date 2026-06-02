from __future__ import annotations
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Use a min-heap to efficiently track the smallest element among k lists
        # Time: O(N log k) where N is total nodes, k is number of lists
        # Space: O(k) for the heap
        
        # Edge case: empty input or all lists are None
        if not lists:
            return None
        
        # Initialize heap with the head of each non-empty list
        # Heap stores tuples: (node_value, list_index, node)
        # list_index serves as tiebreaker to avoid comparing ListNode objects
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        # Build the merged list using a dummy head for cleaner code
        dummy = ListNode(0)
        current = dummy
        
        # Process nodes in sorted order by continuously extracting min from heap
        while min_heap:
            val, list_idx, node = heapq.heappop(min_heap)
            
            # Attach the smallest node to result
            current.next = node
            current = current.next
            
            # If this list has more nodes, push the next node to heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, list_idx, node.next))
        
        return dummy.next