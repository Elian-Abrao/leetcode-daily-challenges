class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Leverage BST property: left subtree < node < right subtree
        # The LCA is the first node where p and q split into different subtrees
        # (or where one of them equals the current node)
        
        current = root
        
        while current:
            # Both p and q are in the left subtree
            # Since current.val > both, we go left to find a smaller ancestor
            if p.val < current.val and q.val < current.val:
                current = current.left
            
            # Both p and q are in the right subtree
            # Since current.val < both, we go right to find a larger ancestor
            elif p.val > current.val and q.val > current.val:
                current = current.right
            
            # Split point found: one is on the left, one is on the right,
            # or current equals p or q. This is the LCA by definition.
            else:
                return current
        
        # Should never reach here given the problem constraints (p and q exist in BST)
        return None