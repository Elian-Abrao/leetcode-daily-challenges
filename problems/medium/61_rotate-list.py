from __future__ import annotations
from typing import Optional

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: empty list or single node or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Calculate the length of the list and find the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Normalize k to avoid unnecessary full rotations
        # Since rotating by length brings us back to the original position
        k = k % length
        
        # If k is 0 after normalization, no rotation needed
        if k == 0:
            return head
        
        # Step 3: Find the new tail (at position length - k - 1 from start)
        # The new head will be at position length - k from start
        # We need to traverse to the node just before the new head
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # Step 4: Perform the rotation
        # The node after new_tail becomes the new head
        new_head = new_tail.next
        
        # Break the link to form the new tail
        new_tail.next = None
        
        # Connect the old tail to the old head to complete the rotation
        tail.next = head
        
        return new_head