from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional['ListNode'], k: int) -> Optional['ListNode']:
        if not head or not head.next or k == 0:
            return head

        # compute length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k_mod = k % length
        if k_mod == 0:
            return head

        # make circular
        tail.next = head

        # find new tail: node at position length - k_mod
        steps_to_new_tail = length - k_mod - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head