from __future__ import annotations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: TreeNode | None) -> TreeNode | None:
        # Base case: empty node remains empty
        if root is None:
            return None

        # Post-order traversal: prune children first
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # If after pruning, the node has no children and its value is 0,
        # the entire subtree rooted here contains no 1 → remove it.
        if root.left is None and root.right is None and root.val == 0:
            return None

        # Otherwise keep the node (children may already be pruned)
        return root