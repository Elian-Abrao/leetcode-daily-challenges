from __future__ import annotations

class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        # Dummy node simplifies linking; its right child becomes the new root.
        dummy = TreeNode(0)
        cur = dummy          # Pointer to the last node in the constructed chain
        stack = []           # Explicit stack for iterative in-order traversal
        node = root

        # Standard in-order traversal using a stack
        while stack or node:
            # Drill down to the leftmost node
            while node:
                stack.append(node)
                node = node.left

            # Pop the node with the smallest value among the unprocessed ones
            node = stack.pop()

            # Create a new node (avoids disturbing the original tree structure)
            # and attach it as the right child of the previous node in the chain.
            cur.right = TreeNode(node.val)
            cur = cur.right

            # Move to the right subtree to continue in-order traversal
            node = node.right

        # The dummy's right child is the root of the rearranged tree
        return dummy.right