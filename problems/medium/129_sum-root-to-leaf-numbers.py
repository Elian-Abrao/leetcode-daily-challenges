from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Use DFS to traverse all root-to-leaf paths
        # Accumulate the number formed by digits along the path
        # Sum all leaf numbers
        
        def dfs(node: Optional[TreeNode], current_number: int) -> int:
            # Base case: empty node contributes nothing
            if not node:
                return 0
            
            # Build the number by appending current digit
            # Shift previous digits left by multiplying by 10
            current_number = current_number * 10 + node.val
            
            # Leaf node: return the complete number formed along this path
            if not node.left and not node.right:
                return current_number
            
            # Internal node: sum contributions from both subtrees
            # Each subtree will continue building numbers from current_number
            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)
            
            return left_sum + right_sum
        
        # Start DFS from root with initial number 0
        return dfs(root, 0)