from __future__ import annotations

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """
        Returns the maximum depth of an N-ary tree.
        Depth is defined as the number of nodes along the longest root-to-leaf path.
        """
        # Empty tree has depth 0
        if not root:
            return 0

        # Compute the maximum depth among all children,
        # treating an empty children list as depth 0.
        max_child_depth = max(
            (self.maxDepth(child) for child in root.children if child),
            default=0
        )

        # Depth of current node = 1 + deepest child's depth
        return 1 + max_child_depth