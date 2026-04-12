from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional['TreeNode'], key: int) -> Optional['TreeNode']:
        """
        Delete a node with value 'key' in a BST and return the new root.
        The standard BST deletion cases:
        - Node has no left child: replace with right child.
        - Node has no right child: replace with left child.
        - Node has two children: replace with inorder successor (min in right subtree),
          then delete that successor node.
        This implementation is strictly O(height of tree) on average.
        """
        if root is None:
            return None

        # Recurse down the tree to locate the node to delete.
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            # Node to delete found.
            # Case 1: Node has no left child -> replace with right subtree.
            if root.left is None:
                return root.right
            # Case 2: Node has no right child -> replace with left subtree.
            if root.right is None:
                return root.left
            # Case 3: Node has two children -> find inorder successor (min in right subtree).
            min_larger_node = self._min_value_node(root.right)
            # Copy the inorder successor's value to current node.
            root.val = min_larger_node.val
            # Delete the inorder successor from the right subtree.
            root.right = self.deleteNode(root.right, min_larger_node.val)
            return root

    def _min_value_node(self, node: 'TreeNode') -> 'TreeNode':
        """
        Return the node with the minimum value in a non-empty binary search tree.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current