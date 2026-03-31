class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # The problem guarantees p and q exist, but guarding against an empty tree
        # keeps the method well-behaved for unexpected callers.
        if root is None:
            return None

        # If one target is the other, that node is trivially the LCA.
        if p is q:
            return p

        # Build parent pointers iteratively to avoid recursion depth issues on
        # highly skewed trees, which are allowed by the constraints.
        parent = {root: None}
        stack = [root]

        # Stop the traversal as soon as both targets are discovered.
        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left is not None:
                parent[node.left] = node
                stack.append(node.left)

            if node.right is not None:
                parent[node.right] = node
                stack.append(node.right)

        # Record every ancestor of p, including p itself, because a node may be
        # the ancestor of itself under the LCA definition.
        ancestors_of_p = set()
        current = p
        while current is not None:
            ancestors_of_p.add(current)
            current = parent[current]

        # The first ancestor of q that also belongs to p's ancestor chain is the
        # lowest common ancestor, because we walk upward from q.
        current = q
        while current not in ancestors_of_p:
            current = parent[current]

        return current