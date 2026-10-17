from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        # Map each value to its index in postorder for O(1) lookup
        post_index = {val: i for i, val in enumerate(postorder)}
        n = len(preorder)

        # Recursive helper using index ranges (exclusive end)
        def build(pre_start: int, pre_end: int, post_start: int, post_end: int) -> Optional[TreeNode]:
            if pre_start >= pre_end:
                return None
            # Root is the first element in preorder
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # If only one node, no children
            if pre_start + 1 == pre_end:
                return root

            # The left child's root (if exists) is the element after root in preorder
            left_root_val = preorder[pre_start + 1]
            # Find its position in postorder to determine left subtree size
            left_root_post_idx = post_index[left_root_val]
            # Number of nodes in the left subtree = (position in postorder - post_start) + 1
            left_size = left_root_post_idx - post_start + 1

            # Recursively construct left subtree (preorder indices after root)
            root.left = build(pre_start + 1, pre_start + 1 + left_size,
                              post_start, post_start + left_size)
            # Right subtree uses the remaining indices
            root.right = build(pre_start + 1 + left_size, pre_end,
                               post_start + left_size, post_end - 1)  # exclude the root from postorder

            return root

        return build(0, n, 0, n)