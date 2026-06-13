from __future__ import annotations
from typing import Optional, List
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Edge case: empty tree
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        # Level-order traversal (BFS)
        # For each level, we only need the rightmost visible node
        while queue:
            level_size = len(queue)
            
            # Process all nodes at current level
            for i in range(level_size):
                node = queue.popleft()
                
                # The last node processed in this level is the rightmost visible one
                if i == level_size - 1:
                    result.append(node.val)
                
                # Add children for next level (left before right maintains order)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result