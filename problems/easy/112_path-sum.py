from __future__ import annotations
from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: empty tree has no root-to-leaf paths
        if not root:
            return False
        
        # Check if we're at a leaf node (no children)
        if not root.left and not root.right:
            # At leaf: check if current path sum equals targetSum
            return root.val == targetSum
        
        # Recursively check left and right subtrees
        # Subtract current node's value from targetSum for child nodes
        remaining = targetSum - root.val
        
        # Return True if either left or right subtree has a valid path
        return (self.hasPathSum(root.left, remaining) or 
                self.hasPathSum(root.right, remaining))