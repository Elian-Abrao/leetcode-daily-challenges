from __future__ import annotations

class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        # Global maximum path length (in edges) seen so far.
        self.ans = 0

        def dfs(node: TreeNode | None) -> int:
            """
            Returns the length of the longest downward univalue path starting
            at `node` (measured in edges).  This is essentially the longest
            "arm" of equal-valued nodes extending from `node` into its children.
            """
            if not node:
                return 0

            # Recursively compute arm lengths from children.
            left_len = dfs(node.left)
            right_len = dfs(node.right)

            # Arm from node going left: possible only if left child exists and
            # shares the same value as node.  Its length is the child's longest
            # down arm plus the edge (node -> child).
            left_arm = left_len + 1 if node.left and node.left.val == node.val else 0
            # Same logic for right arm.
            right_arm = right_len + 1 if node.right and node.right.val == node.val else 0

            # A path that goes through the current node can combine left and
            # right arms (they both have the same value as node).
            self.ans = max(self.ans, left_arm + right_arm)

            # Return the longer arm to the parent so it can extend its own path.
            return max(left_arm, right_arm)

        dfs(root)
        return self.ans