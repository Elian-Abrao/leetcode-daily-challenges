from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        """
        Returns the minimum absolute difference between any two nodes in a BST.
        Uses iterative inorder traversal to process values in sorted order,
        then tracks the minimum difference between consecutive values.
        """
        stack = []
        current = root
        prev_val = None          # Value of the previously visited node in inorder
        min_diff = float('inf')  # Initialize to infinity

        # Standard iterative inorder traversal using a stack
        while stack or current:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # Pop the top node (inorder next)
            current = stack.pop()
            val = current.val

            # If we have a previous value, compute the difference
            if prev_val is not None:
                diff = val - prev_val          # Since inorder is increasing, diff is positive
                if diff < min_diff:
                    min_diff = diff
                    # Early exit: smallest possible difference is 0 (duplicate values)
                    if min_diff == 0:
                        return 0

            prev_val = val
            # Move to the right subtree
            current = current.right

        # In a valid BST with >=2 nodes, min_diff will have been updated
        return int(min_diff)