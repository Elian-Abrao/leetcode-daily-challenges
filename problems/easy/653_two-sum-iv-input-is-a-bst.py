from __future__ import annotations
from typing import Optional, Set

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Returns True if there exist two elements in the BST whose sum equals k.
        Uses DFS traversal with a hash set for O(1) complement lookup.
        Time: O(n) where n is the number of nodes
        Space: O(n) for the set in worst case (when complement is never found early)
        """
        seen: Set[int] = set()
        
        def dfs(node: Optional[TreeNode]) -> bool:
            """DFS helper that returns True if a valid pair is found."""
            if not node:
                return False
            
            # Check if the complement (k - current node's value) has been seen
            complement = k - node.val
            if complement in seen:
                return True
            
            # Add current value to the set before exploring children
            seen.add(node.val)
            
            # Recursively search left and right subtrees
            # Early exit if either subtree contains a valid pair
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)