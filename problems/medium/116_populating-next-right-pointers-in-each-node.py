from __future__ import annotations

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Edge case: empty tree
        if not root:
            return None
        
        # Start with the root level
        leftmost = root
        
        # Process level by level
        # leftmost represents the leftmost node of the current level
        while leftmost.left:  # While there's a next level (perfect binary tree property)
            # Traverse the current level using the next pointers we've already set
            current = leftmost
            
            while current:
                # Connect current's left child to right child
                current.left.next = current.right
                
                # Connect current's right child to next node's left child (if next exists)
                if current.next:
                    current.right.next = current.next.left
                
                # Move to the next node in the current level
                current = current.next
            
            # Move down to the next level
            leftmost = leftmost.left
        
        return root