from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        Converts a binary tree to a string in preorder with parentheses.
        Rules:
        - Each node is represented by its integer value.
        - If a node has at least one child, its children are enclosed in parentheses.
        - If a node has no left child but a right child, we output "()" for the left child
          to preserve the tree structure.
        - Empty parentheses are omitted when they are unnecessary (i.e., when a node has only
          a left child or no children).
        """
        # Base case: empty node yields empty string.
        if root is None:
            return ""

        # Start with the current node's value.
        result = str(root.val)

        # Determine if we need parentheses for the left child.
        # Condition: if there is a left child OR a right child (to handle the special case
        # of a missing left child when a right child exists).
        if root.left or root.right:
            # Recursively convert left subtree. If left is None, recursion returns ""
            # which gives us "()" as required for the empty-left-with-right case.
            result += "(" + self.tree2str(root.left) + ")"

        # Right child parentheses are only added if the right child actually exists.
        if root.right:
            result += "(" + self.tree2str(root.right) + ")"

        return result