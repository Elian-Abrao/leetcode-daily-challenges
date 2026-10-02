from typing import Optional, Dict, Tuple

# Definition for a binary tree node (provided by LeetCode).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Returns the diameter (longest path in edges) of a binary tree.
        Uses iterative post-order DFS to avoid recursion depth issues.
        """
        if not root:
            return 0

        # Stack stores (node, visited_children_flag).
        # True = children have been processed, compute height now.
        stack: List[Tuple[TreeNode, bool]] = [(root, False)]
        # Map each node to its computed height (max edges to leaf).
        height: Dict[TreeNode, int] = {}
        max_diameter = 0

        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if not visited:
                # First time: push back with flag, then push children.
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                # Children are already processed; compute height and candidate diameter.
                left_h = height.get(node.left, 0)   # 0 if child is None
                right_h = height.get(node.right, 0)
                # Diameter that passes through this node.
                max_diameter = max(max_diameter, left_h + right_h)
                # Height of current node: one edge to deeper child.
                height[node] = 1 + max(left_h, right_h)

        return max_diameter