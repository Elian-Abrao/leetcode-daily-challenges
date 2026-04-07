from __future__ import annotations

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Empty list or a single node is already "pair-swapped".
        if head is None or head.next is None:
            return head

        # Dummy node removes special handling for swaps affecting the head.
        dummy = ListNode(0, head)
        prev = dummy

        # Maintain the invariant:
        # - prev.next is the first node of the next pair to process.
        # - everything before prev is already correctly linked.
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Rewire only pointers, never node values, as required.
            first.next = second.next
            second.next = first
            prev.next = second

            # Move to the tail of the swapped pair for the next iteration.
            prev = first

        # Dummy.next always points to the current real head.
        return dummy.next