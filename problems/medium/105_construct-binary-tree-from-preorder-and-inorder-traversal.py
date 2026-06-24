from __future__ import annotations
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Key insight: 
        # - Preorder gives us the root first, then left subtree, then right subtree
        # - Inorder gives us left subtree, then root, then right subtree
        # - Using the root from preorder, we can split inorder into left and right parts
        
        # Build a map for O(1) lookup of indices in inorder array
        # This avoids O(n) search for each recursive call
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Track current position in preorder traversal
        self.preorder_idx = 0
        
        def build(in_left: int, in_right: int) -> Optional[TreeNode]:
            # Base case: no elements to construct the tree
            if in_left > in_right:
                return None
            
            # The current root is at preorder_idx in preorder array
            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            
            # Move to next element in preorder for subsequent recursive calls
            self.preorder_idx += 1
            
            # Find the index of root in inorder to determine left and right subtrees
            root_idx_in_inorder = inorder_index_map[root_val]
            
            # Build left subtree first (preorder visits left before right)
            # Left subtree contains elements from in_left to root_idx - 1 in inorder
            root.left = build(in_left, root_idx_in_inorder - 1)
            
            # Build right subtree
            # Right subtree contains elements from root_idx + 1 to in_right in inorder
            root.right = build(root_idx_in_inorder + 1, in_right)
            
            return root
        
        # Start building from the entire inorder array range
        return build(0, len(inorder) - 1)