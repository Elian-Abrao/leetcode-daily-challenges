from __future__ import annotations

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Recursive divide-and-conquer is optimal here:
        # choosing the middle element keeps subtree sizes as even as possible.
        def build(left: int, right: int) -> Optional[TreeNode]:
            # Empty interval means no node belongs here.
            if left > right:
                return None

            # Middle index produces a height-balanced BST.
            mid = (left + right) // 2

            # The array is already sorted, so nums[mid] is the root of this segment.
            node = TreeNode(nums[mid])

            # Left segment contains smaller values; right segment contains larger values.
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        # Handles all valid inputs, including the smallest size of 1.
        return build(0, len(nums) - 1)