from __future__ import annotations
from typing import Optional, List

class Solution:
    def binaryTreePaths(self, root: Optional['TreeNode']) -> List[str]:
        if root is None:
            return []
        res: List[str] = []
        def dfs(node: 'TreeNode', path: str) -> None:
            if node.left is None and node.right is None:
                res.append(path + str(node.val))
                return
            next_path = path + str(node.val) + "->"
            if node.left:
                dfs(node.left, next_path)
            if node.right:
                dfs(node.right, next_path)
        dfs(root, "")
        return res