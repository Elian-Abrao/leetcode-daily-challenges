from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Edge case: empty tree
        if not root:
            return 0
        
        # Key insight: for a complete binary tree, we can leverage the structure
        # to achieve O(log^2 n) time instead of O(n)
        
        # Strategy: recursively check if subtrees are perfect binary trees
        # If left and right heights are equal, the tree is perfect: count = 2^h - 1
        # Otherwise, recurse on both subtrees
        
        def get_height(node: Optional[TreeNode]) -> int:
            # Height is the length of the leftmost path (complete tree property)
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        
        if left_height == right_height:
            # Left subtree is a perfect binary tree of height left_height
            # Total nodes in left subtree = 2^left_height - 1
            # Add 1 for root, then count right subtree
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is a perfect binary tree of height right_height
            # (left_height must be right_height + 1 in a complete tree)
            # Total nodes in right subtree = 2^right_height - 1
            # Add 1 for root, then count left subtree
            return (1 << right_height) + self.countNodes(root.left)