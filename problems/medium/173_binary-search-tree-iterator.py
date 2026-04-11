from typing import Optional

class BSTIterator:
    def __init__(self, root: Optional['TreeNode']):
        # Stack to store the path to the next smallest node
        self.stack = []
        # Initialize by pushing all the left children from root
        self._push_left(root)

    def _push_left(self, node: Optional['TreeNode']) -> None:
        # Traverse left spine and push nodes onto the stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # The top of the stack is the next smallest element
        node = self.stack.pop()
        value = node.val
        # If there is a right subtree, process its left spine
        if node.right:
            self._push_left(node.right)
        return value

    def hasNext(self) -> bool:
        # There exists a next element if the stack is non-empty
        return bool(self.stack)