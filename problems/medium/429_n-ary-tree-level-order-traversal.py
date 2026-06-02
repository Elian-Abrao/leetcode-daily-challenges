from typing import List, Optional
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        result = []
        # Use a deque for efficient BFS queue operations
        queue = deque([root])
        
        # Standard BFS with level tracking
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add all children to queue for next level
                # children is a list (or None), so we need to check and iterate
                if node.children:
                    for child in node.children:
                        queue.append(child)
            
            result.append(current_level)
        
        return result