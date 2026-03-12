from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's cycle detection uses two runners:
        # - slow moves 1 step
        # - fast moves 2 steps
        # If a cycle exists, they must eventually meet inside the loop.
        slow = head
        fast = head

        # If fast reaches the end, the list is acyclic.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # Identity comparison is required: two pointers meeting at
            # the exact same node proves a cycle regardless of node values.
            if slow is fast:
                return True

        # Covers empty list, single node without self-loop, and any finite list.
        return False