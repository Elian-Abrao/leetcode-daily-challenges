from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge case: if left == right, no reversal needed
        if left == right:
            return head
        
        # Create a dummy node to handle edge case where left == 1
        # This avoids special-casing the head reversal
        dummy = ListNode(0)
        dummy.next = head
        
        # Step 1: Navigate to the node just before position `left`
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        # `prev` now points to the node before the reversal segment
        # `current` is the first node to be reversed
        current = prev.next
        
        # Step 2: Reverse the sublist from position `left` to `right`
        # We use the iterative pointer reversal technique
        # We'll reverse (right - left) links
        
        # `current` will end up as the last node in the reversed segment
        # We need to remember it to connect it to the node after `right`
        tail_of_reversed = current
        
        prev_in_segment = None
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev_in_segment
            prev_in_segment = current
            current = next_node
        
        # After the loop:
        # - `prev_in_segment` is the new head of the reversed segment (was at position `right`)
        # - `current` is the node immediately after position `right`
        # - `tail_of_reversed` is the node that was originally at position `left`
        
        # Step 3: Connect the reversed segment back to the list
        # Connect the node before `left` to the new head of reversed segment
        prev.next = prev_in_segment
        
        # Connect the tail of reversed segment to the node after `right`
        tail_of_reversed.next = current
        
        # Return the new head (dummy.next handles case where left == 1)
        return dummy.next