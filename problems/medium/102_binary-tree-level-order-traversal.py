from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional['TreeNode']) -> List[List[int]]:
        # Return empty for empty tree
        if root is None:
            return []
        
        result: List[List[int]] = []
        q = deque([root])  # BFS queue
        
        # Process level by level
        while q:
            level_size = len(q)
            level_values: List[int] = []
            
            for _ in range(level_size):
                node = q.popleft()
                level_values.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(level_values)
        
        return result