from __future__ import annotations
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True  # Flag to track direction of traversal
        
        # Standard BFS with level-order traversal
        while queue:
            level_size = len(queue)
            level_values = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                
                # Add children for next level (always left to right in queue)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse the level if we're going right to left
            if not left_to_right:
                level_values.reverse()
            
            result.append(level_values)
            
            # Toggle direction for next level
            left_to_right = not left_to_right
        
        return result