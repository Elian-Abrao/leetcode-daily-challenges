from typing import List

# Definition for a Node.
# class Node:
#     def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
#         self.val = val
#         self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Iterative postorder traversal for an n-ary tree.
        # Use a stack to simulate a modified preorder (root, rightmost subtree, ..., leftmost subtree),
        # then reverse the result to obtain the correct postorder (leftmost subtree, ..., rightmost subtree, root).
        if not root:
            return []

        stack = [root]
        result = []  # This stores the "reversed preorder" sequence.

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push all children. Since the stack is LIFO, children are popped
            # in reverse order, which is exactly what we need for the reversal trick.
            if node.children:
                stack.extend(node.children)

        # Reversing the preorder-like list yields the correct postorder traversal.
        return result[::-1]