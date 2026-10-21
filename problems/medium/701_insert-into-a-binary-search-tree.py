from __future__ import annotations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        Inserts a value into a Binary Search Tree and returns the root.
        Uses an iterative approach to avoid recursion depth issues.
        """
        # Case 1: empty tree – create and return the new node as root
        if root is None:
            return TreeNode(val)

        # Case 2: tree is non‑empty – traverse to find the insertion point
        cur = root
        while True:
            # Since val is guaranteed not to exist, we compare and go left/right
            if val < cur.val:
                if cur.left is None:
                    # Found the spot: attach as left child
                    cur.left = TreeNode(val)
                    break
                cur = cur.left
            else:  # val > cur.val
                if cur.right is None:
                    cur.right = TreeNode(val)
                    break
                cur = cur.right

        return root