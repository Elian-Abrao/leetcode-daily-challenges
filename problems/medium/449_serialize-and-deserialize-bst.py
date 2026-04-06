from __future__ import annotations

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        values = []
        stack = [root]

        while stack:
            node = stack.pop()
            values.append(str(node.val))
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        preorder = list(map(int, data.split(",")))
        root = TreeNode(preorder[0])
        stack = [root]

        for value in preorder[1:]:
            node = TreeNode(value)

            if value < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                parent = None
                while stack and stack[-1].val < value:
                    parent = stack.pop()
                parent.right = node
                stack.append(node)

        return root


class Solution(Codec):
    pass