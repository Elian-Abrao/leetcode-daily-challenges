from __future__ import annotations
from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional['ListNode'], k: int) -> Optional['ListNode']:
        # Edge case: if k is 1 or list is empty, no reversal needed
        if not head or k == 1:
            return head
        
        # Use a dummy node to simplify edge cases with head manipulation
        dummy = type('ListNode', (), {'val': 0, 'next': head})()
        dummy.next = head
        
        # prev_group_end tracks the last node of the previous reversed group
        prev_group_end = dummy
        
        while True:
            # Check if there are k nodes remaining to reverse
            kth_node = self._get_kth_node(prev_group_end, k)
            if not kth_node:
                # Less than k nodes left, leave them as is
                break
            
            # Save the start of the next group
            next_group_start = kth_node.next
            
            # Reverse the current k-group
            # Returns new head and tail of reversed segment
            new_head, new_tail = self._reverse_segment(prev_group_end.next, kth_node)
            
            # Connect the previous group to the newly reversed group
            prev_group_end.next = new_head
            # Connect the reversed group to the next segment
            new_tail.next = next_group_start
            
            # Move prev_group_end to the end of the current reversed group
            prev_group_end = new_tail
        
        return dummy.next
    
    def _get_kth_node(self, start, k: int) -> Optional['ListNode']:
        """
        Returns the k-th node from start (not including start itself).
        Returns None if fewer than k nodes exist.
        """
        current = start
        for _ in range(k):
            current = current.next
            if not current:
                return None
        return current
    
    def _reverse_segment(self, start, end) -> tuple:
        """
        Reverses nodes from start to end (inclusive).
        Returns (new_head, new_tail) where:
        - new_head is the original end node (now the first)
        - new_tail is the original start node (now the last)
        
        Time: O(k) where k is the number of nodes in the segment
        Space: O(1) - only pointer manipulation
        """
        prev = None
        current = start
        # Store the original start as it will become the tail
        new_tail = start
        
        # Reverse pointers until we go past the end node
        while prev != end:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # prev now points to end (the new head)
        return prev, new_tail