from __future__ import annotations

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # The input guarantees at least one node, but guarding empty input keeps
        # the method robust and avoids surprising failures in non-LeetCode usage.
        if not traversal:
            return None

        n = len(traversal)
        index = 0

        # Stack invariant:
        # stack[d] is the node at depth d on the current root-to-node path.
        stack = []

        while index < n:
            depth = 0

            # Count dashes to determine the depth of the next node.
            while index < n and traversal[index] == "-":
                depth += 1
                index += 1

            # Parse the full numeric value; values can have multiple digits.
            value = 0
            while index < n and traversal[index].isdigit():
                value = value * 10 + (ord(traversal[index]) - ord("0"))
                index += 1

            node = TreeNode(value)

            # Move back to the parent depth. Any deeper nodes are no longer
            # on the active path once we start a sibling subtree.
            while len(stack) > depth:
                stack.pop()

            if stack:
                parent = stack[-1]

                # Preorder visits left child before right child, and the problem
                # guarantees a single child is always on the left.
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

            stack.append(node)

        # The root is always the first node pushed and remains at index 0.
        return stack[0]