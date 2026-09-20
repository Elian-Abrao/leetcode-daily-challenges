from __future__ import annotations

class Solution:
    def trimBST(self, root: TreeNode | None, low: int, high: int) -> TreeNode | None:
        # Base case: empty subtree
        if root is None:
            return None

        # If current node is outside [low, high], we need to trim it away.
        # Since it's a BST, if it's less than low, its entire left subtree is also too small.
        # So we recursively trim the right subtree (which might contain valid nodes).
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # Similarly, if current node is greater than high, the entire right subtree is too large.
        # Recursively trim the left subtree.
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # Current node is within bounds. 
        # Recursively trim both subtrees in-place and return the current node.
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root