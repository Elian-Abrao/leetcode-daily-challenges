from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Convert BST to Greater Tree in-place using reverse inorder traversal.
        Accumulate the sum of all larger values seen so far.
        """
        # Accumulator for the running sum of visited nodes (all greater values).
        running_sum = 0

        def reverse_inorder(node: Optional[TreeNode]) -> None:
            """
            Perform a right-root-left traversal.
            Update node.val by adding the current running_sum, then update running_sum.
            """
            nonlocal running_sum
            if not node:
                return

            # First, process the right subtree (all larger values).
            reverse_inorder(node.right)

            # Current node gets the original value plus all larger values seen so far.
            node.val += running_sum

            # Update running_sum to include this node's original value (before update).
            # Since we already added running_sum to node.val, we need the original val.
            # But node.val is now new value; we need the original node.val before increment.
            # We saved the original? Simpler: just set running_sum to node.val (which already includes previous running_sum).
            # Because node.val = old_val + running_sum_old. Now running_sum becomes new value.
            running_sum = node.val

            # Finally, process left subtree (smaller values will add this new running_sum).
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root