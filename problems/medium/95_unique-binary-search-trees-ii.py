from __future__ import annotations

from functools import lru_cache
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Defensive guard even though the constraints start at 1.
        if n <= 0:
            return []

        def clone(node: Optional[TreeNode]) -> Optional[TreeNode]:
            # Cached subtrees must be copied before reuse to avoid shared nodes
            # across different answers.
            if node is None:
                return None
            return TreeNode(node.val, clone(node.left), clone(node.right))

        @lru_cache(maxsize=None)
        def build(left: int, right: int) -> tuple[Optional[TreeNode], ...]:
            # Empty interval contributes one valid "empty subtree" choice.
            if left > right:
                return (None,)

            trees = []

            # Try every value as root; BST property then fixes both ranges.
            for root_value in range(left, right + 1):
                left_subtrees = build(left, root_value - 1)
                right_subtrees = build(root_value + 1, right)

                # Cartesian product of valid left/right subtrees for this root.
                for left_root in left_subtrees:
                    for right_root in right_subtrees:
                        trees.append(
                            TreeNode(
                                root_value,
                                clone(left_root),
                                clone(right_root),
                            )
                        )

            # Tuples are cache-friendly and immutable.
            return tuple(trees)

        return list(build(1, n))