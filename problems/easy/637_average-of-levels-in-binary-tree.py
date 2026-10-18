from __future__ import annotations  # support forward reference in type hints
from collections import deque
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> List[float]:
        """
        Returns a list of averages for each level of the binary tree.
        Uses BFS (level-order traversal) to process nodes level by level.
        Time: O(N), Space: O(max_width) ~ O(N) worst-case.
        """
        if root is None:  # safety, though problem says at least one node
            return []

        result: List[float] = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_count = len(queue)

            # Process all nodes on the current level
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val

                # Enqueue children for the next level, if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Compute and store the average for this level
            result.append(level_sum / level_count)

        return result