from __future__ import annotations
from typing import Optional

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Edge case: empty list
        if not head:
            return None
        
        # Use iterative approach with a stack to handle child lists depth-first
        # This ensures child lists are inserted right after their parent node
        
        curr = head
        
        while curr:
            # If current node has a child, we need to splice it in
            if curr.child:
                # Save the next node (may be None)
                next_node = curr.next
                
                # Connect current node to child list
                curr.next = curr.child
                curr.child.prev = curr
                
                # Find the tail of the child list to reconnect next_node
                child_tail = curr.child
                while child_tail.next:
                    child_tail = child_tail.next
                
                # Clear the child pointer as required
                curr.child = None
                
                # Reconnect the original next node after the child list
                if next_node:
                    child_tail.next = next_node
                    next_node.prev = child_tail
            
            # Move to next node in the flattened list
            curr = curr.next
        
        return head