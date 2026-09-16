from __future__ import annotations
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        Returns the root of one duplicate subtree for each group of identical subtrees.
        Uses a serialization-based approach with unique integer IDs to avoid string concatenation overhead.
        """
        # id_map: (val, left_id, right_id) -> unique integer id
        id_map = {}
        # count: id -> number of occurrences seen so far
        count = {}
        result = []

        def dfs(node: Optional[TreeNode]) -> int:
            """Post-order traversal: returns an integer ID representing the subtree rooted at node."""
            if not node:
                # Use a sentinel ID for null nodes (e.g., -1)
                return -1

            left_id = dfs(node.left)
            right_id = dfs(node.right)

            # Build a tuple key uniquely identifying this subtree structure + values
            key = (node.val, left_id, right_id)

            # Assign a new ID if this key hasn't been seen before
            if key not in id_map:
                id_map[key] = len(id_map)  # IDs start from 0
            subtree_id = id_map[key]

            # Increment frequency count for this subtree ID
            curr_count = count.get(subtree_id, 0) + 1
            count[subtree_id] = curr_count

            # On the second occurrence, we have found a duplicate group;
            # add this node to the result (only once per group)
            if curr_count == 2:
                result.append(node)

            return subtree_id

        dfs(root)
        return result