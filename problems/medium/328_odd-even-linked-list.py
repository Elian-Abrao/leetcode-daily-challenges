from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: empty list or single node
        if not head or not head.next:
            return head
        
        # Initialize pointers for odd and even lists
        # odd starts at first node (index 1), even starts at second node (index 2)
        odd = head
        even = head.next
        even_head = even  # Save the head of even list to connect later
        
        # Traverse the list, separating odd and even indexed nodes
        # Continue while there are nodes to process in the even chain
        while even and even.next:
            # Link current odd node to next odd node (skip the even node)
            odd.next = even.next
            odd = odd.next
            
            # Link current even node to next even node (skip the odd node)
            even.next = odd.next
            even = even.next
        
        # Connect the end of odd list to the head of even list
        odd.next = even_head
        
        return head