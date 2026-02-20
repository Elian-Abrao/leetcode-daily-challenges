from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if not head or not head.next:
            return head

        # compute length
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        def split(start: Optional['ListNode'], size: int) -> Optional['ListNode']:
            if not start:
                return None
            cur = start
            for _ in range(size - 1):
                if cur.next:
                    cur = cur.next
                else:
                    break
            rest = cur.next
            cur.next = None
            return rest

        def merge(l1: Optional['ListNode'], l2: Optional['ListNode']):
            dummy = ListNode(0)
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            while tail.next:
                tail = tail.next
            return dummy.next, tail

        dummy = ListNode(0)
        dummy.next = head
        size = 1
        while size < length:
            prev = dummy
            curr = dummy.next
            while curr:
                left = curr
                right = split(left, size)
                curr = split(right, size)
                merged_head, merged_tail = merge(left, right)
                prev.next = merged_head
                prev = merged_tail
            size <<= 1

        return dummy.next