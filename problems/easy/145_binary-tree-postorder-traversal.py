from __future__ import annotations
from typing import Optional, List

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative postorder traversal using a single stack
        # Postorder: left -> right -> root
        
        # Edge case: empty tree
        if not root:
            return []
        
        result = []
        stack = []
        last_visited = None  # Track last node we processed to avoid revisiting
        current = root
        
        # Two-phase approach:
        # 1. Traverse down to leftmost, pushing nodes onto stack
        # 2. Check if we can visit (no right child or right child already visited)
        while stack or current:
            # Phase 1: Go as far left as possible
            if current:
                stack.append(current)
                current = current.left
            else:
                # Phase 2: Check the top of stack
                peek_node = stack[-1]
                
                # If right child exists and hasn't been visited yet, explore it
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    # Both children processed (or don't exist), visit this node
                    result.append(peek_node.val)
                    last_visited = stack.pop()
        
        return result