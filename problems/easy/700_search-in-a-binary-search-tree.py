from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        Returns the subtree rooted with the node whose value equals val,
        or None if no such node exists.
        Uses the BST property (left child < parent < right child) to navigate
        in O(h) time and O(1) extra space.
        """
        current = root
        while current is not None:
            if current.val == val:
                return current                # found the target node
            if val < current.val:
                current = current.left        # search left subtree
            else:
                current = current.right       # search right subtree
        return None                           # value not present