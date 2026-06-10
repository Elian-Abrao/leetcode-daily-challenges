from __future__ import annotations
from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorder list from L0->L1->...->Ln-1->Ln to L0->Ln->L1->Ln-1->L2->Ln-2->...
        
        Strategy:
        1. Find the middle of the list using slow/fast pointers
        2. Reverse the second half
        3. Merge the two halves alternately
        
        Time: O(n), Space: O(1)
        """
        # Edge case: empty or single node
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list
        # After loop, slow will be at the end of first half
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        # Split the list into two halves
        second_half = slow.next
        slow.next = None  # Cut the list in half
        
        # Reverse the second half
        prev = None
        curr = second_half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second_half = prev  # Now points to the head of reversed second half
        
        # Step 3: Merge the two halves alternately
        # L0->L1->L2 and Ln->Ln-1->... becomes L0->Ln->L1->Ln-1->...
        first = head
        second = second_half
        
        while second:  # Second list might be shorter or equal length
            # Save next pointers before overwriting
            first_next = first.next
            second_next = second.next
            
            # Relink: first -> second -> first.next
            first.next = second
            second.next = first_next
            
            # Move to next pair
            first = first_next
            second = second_next