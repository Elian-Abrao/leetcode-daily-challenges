from __future__ import annotations
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative approach using explicit stack
        # Preorder: root -> left -> right
        # Time: O(n) where n is number of nodes
        # Space: O(h) where h is height (worst case O(n) for skewed tree)
        
        # Handle empty tree
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            # Pop current node and process it
            node = stack.pop()
            result.append(node.val)
            
            # Push right child first (so left is processed first due to stack LIFO)
            # This ensures left subtree is visited before right subtree
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result