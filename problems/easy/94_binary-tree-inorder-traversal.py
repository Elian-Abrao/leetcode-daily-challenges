from __future__ import annotations
from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative approach using explicit stack to simulate call stack
        # Inorder: left -> node -> right
        # Time: O(n), Space: O(h) where h is height (worst case O(n) for skewed tree)
        
        result = []
        stack = []
        current = root
        
        # Continue while there are nodes to process or stack is not empty
        while current or stack:
            # Go as far left as possible, pushing nodes onto stack
            while current:
                stack.append(current)
                current = current.left
            
            # Current is None, so we've reached leftmost node
            # Pop from stack to process
            current = stack.pop()
            result.append(current.val)  # Visit node (inorder position)
            
            # Move to right subtree (will repeat left-traversal if exists)
            current = current.right
        
        return result