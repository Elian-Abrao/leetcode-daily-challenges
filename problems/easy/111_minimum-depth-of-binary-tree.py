from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional["TreeNode"]) -> int:
        # If the tree is empty, depth is 0
        if root is None:
            return 0

        # Use BFS to find the nearest leaf; depth increases level by level
        from collections import deque

        queue = deque([(root, 1)])  # (node, current_depth)

        while queue:
            node, depth = queue.popleft()

            # A leaf node has no children; this depth is the minimum
            if node.left is None and node.right is None:
                return depth

            # Add non-null children to the queue with incremented depth
            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))

        # Fallback (should not be reached for valid trees)
        return 0