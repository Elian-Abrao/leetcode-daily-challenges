from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Inorder traversal of BST yields values in ascending order.
        # The minimum absolute difference is the smallest gap between
        # consecutive elements in that order.
        stack = []
        curr = root
        prev_val = None          # value of the previously visited node
        min_diff = float('inf')  # will store the result

        # Iterative inorder traversal using a stack.
        while stack or curr:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # Pop the node with no left child (or left subtree already processed)
            curr = stack.pop()
            # Process current node
            if prev_val is not None:
                # Use absolute difference to handle any ordering (though BST guarantees sorted)
                diff = abs(curr.val - prev_val)
                if diff < min_diff:
                    min_diff = diff
                    # Shortcut: difference cannot be smaller than 0
                    if min_diff == 0:
                        return 0
            # Update previous value and move to the right subtree
            prev_val = curr.val
            curr = curr.right

        # The problem guarantees at least two nodes, so min_diff is updated.
        return int(min_diff)