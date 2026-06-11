from __future__ import annotations
from typing import Optional

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node is already sorted
        if not head or not head.next:
            return head
        
        # Use merge sort for O(n log n) time complexity
        # Split the list into two halves using slow/fast pointer technique
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is now at the node before the midpoint
        # Split the list into two halves
        mid = slow.next
        slow.next = None  # Cut the list in half
        
        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Merge the two sorted halves
        return self.merge(left, right)
    
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Merge two sorted linked lists
        dummy = l1.__class__(0)
        current = dummy
        
        # Compare nodes from both lists and link them in sorted order
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Attach remaining nodes (at most one list has remaining nodes)
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        
        return dummy.next