from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional["ListNode"], l2: Optional["ListNode"]) -> Optional["ListNode"]:
        dummy = ListNode(0)
        curr = dummy
        p, q = l1, l2
        carry = 0
        while p or q or carry:
            x = p.val if p else 0
            y = q.val if q else 0
            total = x + y + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        return dummy.next