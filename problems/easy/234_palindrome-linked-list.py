from __future__ import annotations
from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Strategy: Find middle using slow/fast pointers, reverse second half, compare both halves
        # Time: O(n), Space: O(1)
        
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list using slow/fast pointer technique
        # Slow moves 1 step, fast moves 2 steps
        # When fast reaches end, slow is at the middle (or start of second half for even length)
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list starting from slow
        # After this, slow points to the head of the reversed second half
        prev = None
        current = slow
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        # prev now points to the head of the reversed second half
        second_half = prev
        
        # Step 3: Compare the first half with the reversed second half
        # We compare node by node from the start and from the reversed second half
        first_half = head
        
        while second_half:  # second_half might be shorter or equal length
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        # Optional: Restore the list to original state (not required by problem)
        # We skip restoration for simplicity and to maintain O(1) space
        
        return True