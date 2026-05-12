from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head to simplify result list construction
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both lists simultaneously, handling carry propagation
        while l1 or l2 or carry:
            # Get current digit values (0 if list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Compute sum of current digits plus carry from previous position
            total = val1 + val2 + carry
            
            # Extract the digit to store (0-9) and new carry (0 or 1)
            carry = total // 10
            digit = total % 10
            
            # Append new node with the computed digit
            current.next = ListNode(digit)
            current = current.next
            
            # Advance pointers in input lists if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the actual result, skipping the dummy head
        return dummy.next