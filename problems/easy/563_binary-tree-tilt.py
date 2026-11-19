from typing import Optional

# Definition for a binary tree node (provided by LeetCode, shown here for clarity):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root: Optional['TreeNode']) -> int:
        """
        Returns the sum of tilts of all nodes in the binary tree.
        Tilt of a node = |sum(left subtree) - sum(right subtree)|.
        """
        total_tilt = 0

        def dfs(node: Optional['TreeNode']) -> int:
            nonlocal total_tilt
            if node is None:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            total_tilt += abs(left_sum - right_sum)

            return node.val + left_sum + right_sum

        dfs(root)
        return total_tilt