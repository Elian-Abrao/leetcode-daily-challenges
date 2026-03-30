from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy heads let us build two stable chains without special-casing
        # the first inserted node in either partition.
        less_dummy = ListNode(0)
        greater_equal_dummy = ListNode(0)

        less_tail = less_dummy
        greater_equal_tail = greater_equal_dummy

        current = head
        while current:
            next_node = current.next
            current.next = None  # Detach now to avoid accidental stale links.

            if current.val < x:
                # Append to the "less than x" chain, preserving original order.
                less_tail.next = current
                less_tail = current
            else:
                # Append to the "greater than or equal to x" chain.
                greater_equal_tail.next = current
                greater_equal_tail = current

            current = next_node

        # Stitch the two chains together; if the first chain is empty,
        # less_dummy.next naturally remains None and the second chain is returned.
        less_tail.next = greater_equal_dummy.next
        return less_dummy.next