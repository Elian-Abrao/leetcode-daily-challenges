from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Use tree DP: each node returns (max_without_rob, max_with_rob)
        # where:
        #   max_without_rob = max money if we DON'T rob this node
        #   max_with_rob = max money if we DO rob this node
        #
        # If we rob current node, we can't rob children (must skip them)
        # If we don't rob current node, we can choose to rob or not rob children
        
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            # Base case: empty node contributes nothing
            if not node:
                return (0, 0)
            
            # Recursively get optimal results from left and right children
            left_without, left_with = dfs(node.left)
            right_without, right_with = dfs(node.right)
            
            # If we rob this node, we must skip direct children
            # So we take their "without rob" values
            rob_current = node.val + left_without + right_without
            
            # If we don't rob this node, we can choose the best option
            # for each child (either rob them or not)
            skip_current = max(left_without, left_with) + max(right_without, right_with)
            
            # Return (max when not robbing current, max when robbing current)
            return (skip_current, rob_current)
        
        # The answer is the maximum of robbing or not robbing the root
        without_root, with_root = dfs(root)
        return max(without_root, with_root)