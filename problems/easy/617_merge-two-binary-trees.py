from __future__ import annotations

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """
        Merge two binary trees by summing overlapping nodes and keeping non‑null
        nodes from either tree. Returns the root of the merged tree.

        Time: O(min(n, m)) where n, m are the number of nodes in each tree.
        Space: O(min(h1, h2)) recursion stack, where h is tree height.
        """
        # If both nodes are missing, the merged node is also missing.
        if not root1 and not root2:
            return None

        # If one side is missing, reuse the existing subtree from the other side.
        # This avoids copying and keeps the solution efficient.
        if not root1:
            return root2
        if not root2:
            return root1

        # Both nodes exist: create a new node with the sum of their values,
        # then recursively merge the left and right children.
        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged