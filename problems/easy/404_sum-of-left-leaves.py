from __future__ import annotations
from typing import Optional

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Handle edge case: empty tree
        if not root:
            return 0
        
        total = 0
        
        # Use iterative DFS with a stack to traverse the tree
        # Each stack entry is (node, is_left_child)
        stack = [(root, False)]
        
        while stack:
            node, is_left = stack.pop()
            
            # Check if current node is a leaf (no children)
            if not node.left and not node.right:
                # Only add to sum if this leaf is a left child
                if is_left:
                    total += node.val
            else:
                # Push right child first so left is processed first (DFS order)
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, True))
        
        return total