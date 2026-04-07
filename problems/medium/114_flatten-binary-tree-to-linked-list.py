from __future__ import annotations

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root

        # Morris-style rewiring keeps the process in-place with O(1) extra space.
        # For each node, splice its left subtree between the node and its right subtree.
        while current:
            if current.left:
                # The preorder sequence is: current, left subtree, right subtree.
                # So we attach the original right subtree after the rightmost node
                # of the left subtree, which is the last node visited there.
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = current.right
                current.right = current.left
                current.left = None  # Required by the flattened list format.

            # Move along the newly formed linked list.
            current = current.right