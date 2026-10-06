from __future__ import annotations
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        """
        Returns the maximum width of a binary tree.
        Width at a level is defined as the number of nodes between the leftmost
        and rightmost non-null nodes (including nulls that would exist in a
        complete binary tree of that level).
        """
        if not root:
            return 0

        max_width = 0
        # BFS queue storing (node, its index in a virtual complete binary tree)
        # Root gets index 0; left child -> 2*idx+1, right child -> 2*idx+2.
        queue = deque()
        queue.append((root, 0))

        while queue:
            level_size = len(queue)
            # The first (leftmost) node's index in this level
            first_idx = queue[0][1]
            # Will be updated to the last (rightmost) node's index
            last_idx = 0

            for _ in range(level_size):
                node, idx = queue.popleft()
                last_idx = idx

                # Enqueue children with their computed indices
                if node.left:
                    queue.append((node.left, 2 * idx + 1))
                if node.right:
                    queue.append((node.right, 2 * idx + 2))

            # Width = last index - first index + 1
            level_width = last_idx - first_idx + 1
            if level_width > max_width:
                max_width = level_width

        return max_width