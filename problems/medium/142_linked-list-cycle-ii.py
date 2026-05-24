from __future__ import annotations
from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Floyd's Cycle Detection Algorithm (Tortoise and Hare)
        # Phase 1: Detect if cycle exists
        # Phase 2: Find the entry point of the cycle
        
        # Edge case: empty list or single node without cycle
        if not head or not head.next:
            return None
        
        # Phase 1: Use slow and fast pointers to detect cycle
        slow = head
        fast = head
        
        # Move slow by 1 step and fast by 2 steps
        # If they meet, there's a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Cycle detected, break to proceed to phase 2
                break
        else:
            # fast reached end, no cycle exists
            return None
        
        # Phase 2: Find the entry point of the cycle
        # Mathematical proof: If slow and fast meet at distance k from cycle start,
        # and the cycle starts at distance m from head, then moving one pointer
        # back to head and advancing both at same speed will make them meet at cycle start.
        # 
        # Reasoning: Let's say:
        # - Distance from head to cycle start = m
        # - Distance from cycle start to meeting point = k
        # - Cycle length = c
        # When they meet: slow traveled m + k, fast traveled m + k + nc (n cycles)
        # Since fast is 2x speed: 2(m + k) = m + k + nc
        # Simplifying: m + k = nc, so m = nc - k = (n-1)c + (c - k)
        # This means distance from head to cycle start equals 
        # distance from meeting point to cycle start (going forward in cycle)
        
        # Reset one pointer to head
        slow = head
        
        # Move both pointers one step at a time
        # They will meet at the cycle entry point
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Both pointers now point to the cycle start
        return slow