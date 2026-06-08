from __future__ import annotations
from typing import Optional, List

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Edge case: empty tree (though problem guarantees at least 1 node)
        if not root:
            return []
        
        result = []
        
        def dfs(node: Optional[TreeNode], path: str) -> None:
            """
            DFS traversal building path string as we go.
            When we reach a leaf, add the complete path to result.
            """
            # Append current node's value to path
            if path:
                path += f"->{node.val}"
            else:
                path = str(node.val)
            
            # Leaf node: no children, so this path is complete
            if not node.left and not node.right:
                result.append(path)
                return
            
            # Recurse on left subtree if it exists
            if node.left:
                dfs(node.left, path)
            
            # Recurse on right subtree if it exists
            if node.right:
                dfs(node.right, path)
        
        dfs(root, "")
        return result