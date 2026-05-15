from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Use a dummy head to simplify edge cases and avoid special-casing the first node
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists, always picking the smaller value
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # At most one list has remaining nodes; attach the non-empty one
        # This handles cases where lists have different lengths
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # Return the actual head (skip dummy node)
        return dummy.next