from __future__ import annotations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode | None) -> TreeNode | None:
        """
        Returns the smallest subtree that contains all the deepest nodes.
        Uses a single DFS to compute both depth and the candidate subtree.
        
        Approach:
        - For each node, recursively compute the depth of its deepest leaf.
        - If both children have the same deepest depth, this node is the LCA
          of those deepest leaves, so it becomes the candidate.
        - Otherwise, propagate the child with the greater depth as the candidate.
        - This naturally finds the lowest common ancestor of all deepest leaves.
        
        Time: O(n), Space: O(n) worst-case (skewed tree).
        """
        def dfs(node: TreeNode | None) -> tuple[int, TreeNode | None]:
            """Return (depth, smallest_subtree_root) for given node."""
            if not node:
                # Base case: depth 0 (empty tree), no subtree.
                return (0, None)

            # Post-order: process children first.
            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)

            if left_depth > right_depth:
                # Deepest leaves are entirely in left subtree.
                return (left_depth + 1, left_subtree)
            elif right_depth > left_depth:
                # Deepest leaves are entirely in right subtree.
                return (right_depth + 1, right_subtree)
            else:
                # Both sides have equally deep leaves.
                # This node becomes the LCA of the deepest leaves.
                return (left_depth + 1, node)

        # The DFS returns the depth and the answer subtree.
        _, answer = dfs(root)
        return answer