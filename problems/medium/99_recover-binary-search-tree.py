from __future__ import annotations
from typing import Optional

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Recover BST where exactly two nodes were swapped.
        Uses Morris traversal for O(1) space complexity.
        
        Key insight: In-order traversal of BST should be sorted.
        When two nodes are swapped, there will be one or two violations
        where a node is greater than its successor.
        
        Case 1: Adjacent nodes swapped -> one violation
        Case 2: Non-adjacent nodes swapped -> two violations
        """
        # Track violations during in-order traversal
        first = second = None  # The two swapped nodes
        prev = None  # Previous node in in-order traversal
        
        current = root
        
        # Morris traversal: in-order without stack (O(1) space)
        while current:
            if current.left is None:
                # Process current node (in-order position)
                if prev and prev.val > current.val:
                    # Found a violation
                    if first is None:
                        # First violation: mark both prev and current
                        first = prev
                        second = current
                    else:
                        # Second violation: update second pointer
                        second = current
                
                prev = current
                current = current.right
            else:
                # Find in-order predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    # Create temporary thread to current
                    predecessor.right = current
                    current = current.left
                else:
                    # Thread exists, remove it and process current
                    predecessor.right = None
                    
                    # Process current node
                    if prev and prev.val > current.val:
                        if first is None:
                            first = prev
                            second = current
                        else:
                            second = current
                    
                    prev = current
                    current = current.right
        
        # Swap the values of the two misplaced nodes
        if first and second:
            first.val, second.val = second.val, first.val