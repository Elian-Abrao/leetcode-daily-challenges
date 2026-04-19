from __future__ import annotations
from typing import Optional

# Definition for singly-linked list is assumed to be provided by the platform.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has a single node, nothing to remove
        if head is None:
            return None

        current = head
        # Iterate through the list, removing consecutive duplicates
        while current.next is not None:
            if current.val == current.next.val:
                # Skip the duplicated node
                current.next = current.next.next
            else:
                # Move forward when there is no duplication
                current = current.next

        return head