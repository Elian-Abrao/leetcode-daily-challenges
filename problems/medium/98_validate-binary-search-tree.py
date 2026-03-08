from __future__ import annotations

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # An empty tree is a valid BST by definition.
        if root is None:
            return True

        stack = []
        current = root
        previous_value = None

        # In-order traversal of a BST must produce a strictly increasing sequence.
        while stack or current:
            # Go as far left as possible to reach the next smallest value.
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()

            # Equality is also invalid because BST ordering is strict.
            if previous_value is not None and current.val <= previous_value:
                return False

            # Keep the last visited value as the lower bound for future nodes.
            previous_value = current.val

            # After visiting a node, the next candidates come from its right subtree.
            current = current.right

        # If traversal never breaks the increasing order, the tree is valid.
        return True