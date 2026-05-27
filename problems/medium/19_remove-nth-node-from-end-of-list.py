from __future__ import annotations
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional['ListNode'], n: int) -> Optional['ListNode']:
        # Use two-pointer technique to find nth node from end in one pass
        # The key insight: maintain a gap of n nodes between fast and slow pointers
        
        # Create a dummy node to handle edge case where head itself is removed
        dummy = head.__class__(0)
        dummy.next = head
        
        # Initialize both pointers at dummy
        fast = dummy
        slow = dummy
        
        # Move fast pointer n+1 steps ahead to create gap of n nodes
        # This ensures when fast reaches end, slow is at node before target
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches end
        # Invariant: gap between fast and slow is always n nodes
        while fast is not None:
            fast = fast.next
            slow = slow.next
        
        # Now slow is at the node right before the one to be removed
        # Skip the nth node from end by updating next pointer
        slow.next = slow.next.next
        
        # Return the new head (could be different if original head was removed)
        return dummy.next