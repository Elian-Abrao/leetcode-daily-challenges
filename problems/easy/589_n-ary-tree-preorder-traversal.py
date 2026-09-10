from __future__ import annotations
from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        Iterative preorder traversal of an N-ary tree.
        Uses a stack to emulate the recursive call order.
        Time: O(n) – each node visited once.
        Space: O(n) – worst-case stack depth (skewed tree).
        """
        if not root:
            return []                     # empty tree → empty list

        result = []
        stack = [root]                    # start with the root

        while stack:
            node = stack.pop()            # current node (top of stack)
            result.append(node.val)       # visit root first

            # Push children in reverse order so that the first child
            # is processed next (stack LIFO → maintains left‑to‑right order).
            if node.children:
                # Iterate from last to first to preserve order
                for child in reversed(node.children):
                    stack.append(child)

        return result