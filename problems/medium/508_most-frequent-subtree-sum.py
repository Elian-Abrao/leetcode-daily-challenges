# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from __future__ import annotations
from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        # Use a Counter to record frequencies of each subtree sum.
        freq = Counter()
        
        def dfs(node: TreeNode | None) -> int:
            """Post-order traversal: return the sum of subtree rooted at node."""
            if not node:
                return 0
            # Recursively compute left and right subtree sums.
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            # Current subtree sum = node value + left + right.
            total = node.val + left_sum + right_sum
            # Record this sum's frequency.
            freq[total] += 1
            return total
        
        # Start the recursion; we ignore the returned root sum because we already
        # recorded all subtree sums during traversal.
        dfs(root)
        
        # Find the maximum frequency among all subtree sums.
        max_freq = max(freq.values())
        # Collect all sums that achieve this maximum frequency.
        return [s for s, count in freq.items() if count == max_freq]