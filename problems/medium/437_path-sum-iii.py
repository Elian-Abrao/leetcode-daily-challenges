from __future__ import annotations

from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Empty tree cannot contain any valid downward path.
        if root is None:
            return 0

        # prefix_count[s] = how many times prefix sum s appears on the current root-to-node path.
        # Starting with 0 once lets us count paths that begin at the current traversal root.
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if node is None:
                return 0

            # Extend the running prefix sum with the current node.
            current_sum += node.val

            # If a previous prefix was current_sum - targetSum, the segment between that
            # prefix and this node sums to targetSum.
            total_paths = prefix_count[current_sum - targetSum]

            # Make this prefix available to descendants before exploring them.
            prefix_count[current_sum] += 1

            # Count valid paths in both subtrees while preserving the current path state.
            total_paths += dfs(node.left, current_sum)
            total_paths += dfs(node.right, current_sum)

            # Backtrack so sibling branches do not see prefixes from this branch.
            prefix_count[current_sum] -= 1

            return total_paths

        return dfs(root, 0)