from __future__ import annotations
from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Use a sentinel value to indicate imbalance while computing height
        # This allows single-pass DFS without extra boolean flags
        
        def height(node: Optional[TreeNode]) -> int:
            # Returns height if balanced, -1 if unbalanced
            if not node:
                return 0
            
            # Recursively check left subtree
            left_height = height(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced
            
            # Recursively check right subtree
            right_height = height(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced
            
            # Check balance condition at current node
            if abs(left_height - right_height) > 1:
                return -1  # Current node violates balance property
            
            # Return height of current subtree (max of children + 1)
            return max(left_height, right_height) + 1
        
        # Tree is balanced if height computation doesn't return -1
        return height(root) != -1