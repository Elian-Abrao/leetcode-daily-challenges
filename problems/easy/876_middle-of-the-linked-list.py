from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use slow and fast pointer technique.
        # Slow moves one step, fast moves two steps.
        # When fast reaches the end, slow is at the middle.
        # For even-length lists, slow ends at the second middle node.
        slow = fast = head
        
        # Traverse while fast can make two more steps
        while fast and fast.next:
            slow = slow.next          # move slow one step
            fast = fast.next.next     # move fast two steps
        
        # slow is now pointing to the middle node
        return slow