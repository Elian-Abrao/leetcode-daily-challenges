from __future__ import annotations
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Build a hashmap for quick lookup of indices in inorder traversal
        # This allows O(1) lookup instead of O(n) search for root position
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Track current position in postorder (rightmost unprocessed node)
        # We process postorder from right to left (root -> right -> left)
        self.post_idx = len(postorder) - 1
        
        def build(in_left: int, in_right: int) -> Optional[TreeNode]:
            # Base case: empty subtree
            if in_left > in_right:
                return None
            
            # The current root is at post_idx in postorder
            # Postorder: left subtree, right subtree, root
            # So we process from the end (root first)
            root_val = postorder[self.post_idx]
            root = TreeNode(root_val)
            self.post_idx -= 1
            
            # Find root position in inorder to split left/right subtrees
            # Inorder: left subtree, root, right subtree
            root_idx = inorder_map[root_val]
            
            # CRITICAL: Build right subtree BEFORE left subtree
            # Since we're processing postorder from right to left,
            # after processing root, the next nodes belong to right subtree
            root.right = build(root_idx + 1, in_right)
            root.left = build(in_left, root_idx - 1)
            
            return root
        
        # Start building from the entire range of inorder array
        return build(0, len(inorder) - 1)