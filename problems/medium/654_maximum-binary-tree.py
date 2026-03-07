from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional["TreeNode"]:
        if not nums:
            return None

        stack = []

        for value in nums:
            current = TreeNode(value)

            while stack and stack[-1].val < value:
                current.left = stack.pop()

            if stack:
                stack[-1].right = current

            stack.append(current)

        return stack[0]