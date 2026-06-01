from __future__ import annotations
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: empty tree or leaf node's children
        if root is None:
            return None
        
        # Recursively invert left and right subtrees first
        # This ensures we process bottom-up, though top-down also works
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        
        # Swap the left and right children
        root.left = right_inverted
        root.right = left_inverted
        
        # Return the current node as the new root of this subtree
        return root