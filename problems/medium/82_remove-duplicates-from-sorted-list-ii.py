from __future__ import annotations
from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional['ListNode']) -> Optional['ListNode']:
        # Define ListNode class if not already defined
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
        
        # Use a dummy node to simplify handling edge cases where head itself is a duplicate
        dummy = ListNode(0)
        dummy.next = head
        
        # predecessor points to the last node before the current sublist being checked
        predecessor = dummy
        
        while head:
            # Check if current node is start of duplicates
            # by comparing with next node
            if head.next and head.val == head.next.val:
                # Skip all nodes with this duplicate value
                # We need to remove ALL occurrences, not keep one
                while head.next and head.val == head.next.val:
                    head = head.next
                
                # Now head points to the last duplicate node
                # Move head one more step to skip it entirely
                head = head.next
                
                # Connect predecessor to the node after all duplicates
                predecessor.next = head
            else:
                # Current node is unique (no duplicate with next)
                # Safe to advance predecessor
                predecessor = predecessor.next
                head = head.next
        
        return dummy.next