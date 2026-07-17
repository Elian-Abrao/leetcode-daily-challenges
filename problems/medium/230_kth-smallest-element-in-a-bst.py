from __future__ import annotations
from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Use iterative in-order traversal to find kth smallest element
        # In-order traversal of BST produces sorted sequence
        # Time: O(H + k) where H is height, Space: O(H) for stack
        
        stack = []
        current = root
        count = 0
        
        # Iterative in-order: left -> node -> right
        while current or stack:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node (smallest unvisited in subtree)
            current = stack.pop()
            count += 1
            
            # If we've seen k elements, current is kth smallest
            if count == k:
                return current.val
            
            # Move to right subtree
            current = current.right
        
        # Should never reach here given problem constraints (1 <= k <= n)
        return -1