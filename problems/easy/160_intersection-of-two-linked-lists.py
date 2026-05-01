from __future__ import annotations
from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Two-pointer technique: traverse both lists, then switch to the other list
        # when reaching the end. This synchronizes the pointers at the intersection.
        #
        # Key insight: if lists have different lengths (a and b nodes before intersection,
        # and c nodes in common), then:
        # - pointerA travels: a + c + b steps
        # - pointerB travels: b + c + a steps
        # Both pointers will meet at the intersection node (or both reach None).
        #
        # Time: O(m + n), Space: O(1)
        
        if not headA or not headB:
            return None
        
        pointerA = headA
        pointerB = headB
        
        # Continue until both pointers meet (either at intersection or at None)
        # Each pointer will traverse at most m + n nodes
        while pointerA != pointerB:
            # Move to next node, or switch to the other list's head if at end
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        # Either both are None (no intersection) or both point to intersection node
        return pointerA