import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            # If both trees are empty, they are mirrors.
            if not t1 and not t2:
                return True
            # If only one of the trees is empty, they are not mirrors.
            if not t1 or not t2:
                return False
            
            # For them to be mirrors, their values must be equal,
            # AND t1's left child must mirror t2's right child,
            # AND t1's right child must mirror t2's left child.
            return (t1.val == t2.val and
                    is_mirror(t1.left, t2.right) and
                    is_mirror(t1.right, t2.left))

        # A tree is symmetric if its left and right subtrees are mirrors of each other.
        return is_mirror(root.left, root.right)