from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional['TreeNode']) -> str:
        if not root:
            return ""
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(str(node.val))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional['TreeNode']:
        if not data:
            return None
        vals = list(map(int, data.split(',')))
        self.idx = 0

        def helper(minval, maxval) -> Optional['TreeNode']:
            if self.idx >= len(vals):
                return None
            val = vals[self.idx]
            if val < minval or val > maxval:
                return None
            self.idx += 1
            node = TreeNode(val)
            node.left = helper(minval, val)
            node.right = helper(val, maxval)
            return node

        return helper(float('-inf'), float('inf'))