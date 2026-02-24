from __future__ import annotations

from collections import deque
from typing import Optional


class Codec:
    class _Node:
        __slots__ = ('val', 'left', 'right')
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def serialize(self, root: "TreeNode") -> str:
        """Serialize a binary tree to a string using level-order traversal.
        
        - Represent None as the string "null".
        - Trim trailing "null" values to keep the representation compact.
        - Use a surrounding [] with comma-separated values to resemble common LeetCode formats.
        """
        if root is None:
            return "[]"

        values = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node is None:
                values.append("null")
            else:
                values.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        # Remove trailing nulls that don't affect tree structure
        while values and values[-1] == "null":
            values.pop()

        return "[" + ",".join(values) + "]"

    def deserialize(self, data: str) -> Optional["TreeNode"]:
        """Deserialize a string produced by serialize back into the binary tree.
        
        Accepts formats like: "[1,2,3,null,null,4,5]".
        Returns None for an empty tree "[]".
        """
        if not data:
            return None

        s = data.strip()
        if s == "[]":
            return None

        # Strip surrounding brackets if present
        if s[0] == "[" and s[-1] == "]":
            s = s[1:-1]
        if not s:
            return None

        parts = [p.strip() for p in s.split(",")]
        if not parts or parts[0] == "null":
            return None

        root = self._Node(int(parts[0]))
        q = deque([root])
        i = 1

        while q and i < len(parts):
            node = q.popleft()

            # Left child
            if i < len(parts):
                left_val = parts[i]
                i += 1
                if left_val != "null":
                    node.left = self._Node(int(left_val))
                    q.append(node.left)

            # Right child
            if i < len(parts):
                right_val = parts[i]
                i += 1
                if right_val != "null":
                    node.right = self._Node(int(right_val))
                    q.append(node.right)

        return root