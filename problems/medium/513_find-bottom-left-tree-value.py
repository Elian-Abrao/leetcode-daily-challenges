from __future__ import annotations
from typing import Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Edge case: empty tree (though constraints guarantee at least 1 node)
        if not root:
            return 0
        
        # BFS approach: the last node processed at the deepest level
        # that is the leftmost will be the answer.
        queue = deque([root])
        leftmost_value = root.val
        
        while queue:
            level_size = len(queue)
            
            # First node of current level is the leftmost if we
            # process nodes from left to right.
            leftmost_value = queue[0].val
            
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        # After BFS completes, leftmost_value holds the leftmost
        # value of the last (deepest) level.
        return leftmost_value