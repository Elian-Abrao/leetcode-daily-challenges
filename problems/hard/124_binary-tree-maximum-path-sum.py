from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Track the global maximum path sum across all nodes
        # Initialize to negative infinity to handle all-negative trees
        self.max_sum = float('-inf')
        
        def max_gain(node: Optional[TreeNode]) -> int:
            """
            Returns the maximum sum of a path that:
            1. Starts at this node and goes down to descendants
            2. Does NOT split (goes either left OR right, not both)
            
            This allows the parent to potentially extend the path upward.
            
            As a side effect, we also consider paths that DO split at this node
            (going through both left and right children) and update global max.
            """
            if not node:
                return 0
            
            # Recursively get max gain from left and right subtrees
            # Use max(0, ...) to ignore negative-sum paths (better to not include them)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Consider the path that splits at current node:
            # left_path -> node -> right_path
            # This path cannot be extended upward, but might be the global max
            path_through_node = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, path_through_node)
            
            # Return the max gain if we continue the path upward through this node
            # We can only go one direction (left OR right), so pick the better one
            return node.val + max(left_gain, right_gain)
        
        # Start DFS from root
        max_gain(root)
        
        return self.max_sum