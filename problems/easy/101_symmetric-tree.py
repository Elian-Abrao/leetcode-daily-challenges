from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # A tree is symmetric if left and right subtrees are mirrors of each other
        # We need a helper to compare two subtrees for mirror symmetry
        
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # Both null: symmetric at this level
            if not left and not right:
                return True
            
            # One null, other not: asymmetric
            if not left or not right:
                return False
            
            # Both non-null: values must match AND subtrees must be mirrors
            # Key insight: left's left mirrors right's right, left's right mirrors right's left
            return (left.val == right.val and 
                    isMirror(left.left, right.right) and 
                    isMirror(left.right, right.left))
        
        # Edge case: empty tree is symmetric
        if not root:
            return True
        
        # Check if left and right subtrees of root are mirrors
        return isMirror(root.left, root.right)