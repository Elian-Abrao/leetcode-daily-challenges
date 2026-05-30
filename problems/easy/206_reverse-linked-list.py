from __future__ import annotations
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative approach using three pointers
        # Time: O(n), Space: O(1)
        
        # Handle empty list
        if not head:
            return None
        
        # Initialize pointers:
        # prev: will become the new head after full reversal
        # curr: current node being processed
        prev = None
        curr = head
        
        # Traverse the list and reverse pointers one by one
        while curr:
            # Store next node before we overwrite curr.next
            next_node = curr.next
            
            # Reverse the pointer: current node now points backwards
            curr.next = prev
            
            # Move prev and curr one step forward
            prev = curr
            curr = next_node
        
        # prev now points to the last node, which is the new head
        return prev