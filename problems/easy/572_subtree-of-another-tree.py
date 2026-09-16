from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(
        self, root: TreeNode | None, subRoot: TreeNode | None
    ) -> bool:
        """
        Returns True if subRoot is a subtree of root (including same tree).
        Constraints: root and subRoot are valid trees (>=1 node), but we handle
        None robustly for completeness.
        """
        # An empty tree is always a subtree of any tree.
        if subRoot is None:
            return True
        # Non‑empty subRoot cannot be found in an empty root.
        if root is None:
            return False

        # If the current root matches subRoot exactly, we are done.
        if self._is_same_tree(root, subRoot):
            return True

        # Otherwise, check the left and right subtrees recursively.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(
            root.right, subRoot
        )

    def _is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        Returns True if the two binary trees rooted at p and q are
        structurally identical and have the same node values.
        """
        # Both nodes are None → identical.
        if p is None and q is None:
            return True
        # One is None, the other is not → different.
        if p is None or q is None:
            return False
        # Values must match.
        if p.val != q.val:
            return False

        # Recursively compare left and right subtrees.
        return self._is_same_tree(p.left, q.left) and self._is_same_tree(
            p.right, q.right
        )