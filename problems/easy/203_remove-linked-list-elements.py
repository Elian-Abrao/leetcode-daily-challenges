from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Use a dummy node to simplify head removal cases
        # This avoids special handling when the head itself needs to be removed
        dummy = type('ListNode', (), {'val': 0, 'next': head})()
        
        # Traverse with current pointer starting at dummy
        current = dummy
        
        # Iterate through the list
        while current.next:
            if current.next.val == val:
                # Skip the node with matching value by updating the next pointer
                current.next = current.next.next
            else:
                # Move to the next node only if we didn't remove one
                # This ensures we check consecutive matching values correctly
                current = current.next
        
        # Return the new head (dummy.next handles empty list case)
        return dummy.next