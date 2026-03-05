from __future__ import annotations

from typing import List, Optional
import sys


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional['TreeNode'], targetSum: int) -> List[List[int]]:
        """
        Find all root-to-leaf paths where the sum of node values equals targetSum.

        Approach:
        - Depth-First Search (DFS) with backtracking.
        - Maintain a current path list and the running sum.
        - On reaching a leaf, if sum equals targetSum, record a copy of the path.
        - Use backtracking to revert path state when returning from recursion.

        Complexity:
        - Time: O(n) visiting each node once.
        - Space: O(h) recursion stack + O(k) for the result where h is tree height.
        """
        sys.setrecursionlimit(1000000)

        if root is None:
            return []

        results: List[List[int]] = []
        current_path: List[int] = []

        def dfs(node: Optional['TreeNode'], current_sum: int) -> None:
            if node is None:
                return

            # Include this node in the current path
            current_sum += node.val
            current_path.append(node.val)

            # Check if this is a leaf
            if node.left is None and node.right is None:
                if current_sum == targetSum:
                    # Copy current path as a valid result
                    results.append(current_path.copy())
            else:
                # Continue exploring children
                dfs(node.left, current_sum)
                dfs(node.right, current_sum)

            # Backtrack: remove current node before returning to the caller
            current_path.pop()

        dfs(root, 0)
        return results