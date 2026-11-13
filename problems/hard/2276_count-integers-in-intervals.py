from __future__ import annotations
import random

class CountIntervals:
    """
    Data structure for maintaining a dynamic set of integer intervals.
    Supports adding intervals and querying the total number of distinct
    integers covered (union size).
    
    Implementation uses an implicit treap (Cartesian tree) keyed by
    left endpoint. Each node stores the interval and subtree aggregates:
    total length covered (sub_sum) and maximum right endpoint (sub_max_r).
    """

    class Node:
        __slots__ = ('l', 'r', 'length', 'prio', 'left', 'right',
                     'sub_sum', 'sub_max_r')

        def __init__(self, l: int, r: int) -> None:
            self.l = l
            self.r = r
            self.length = r - l + 1
            # random priority ensures balanced tree expectedly
            self.prio = random.randint(1, 1 << 30)
            self.left = None
            self.right = None
            # subtree aggregates
            self.sub_sum = self.length
            self.sub_max_r = r

    def __init__(self) -> None:
        self.root = None      # root of the treap
        self.total = 0        # total number of distinct integers covered

    # -----------------------------------------------------------------
    #  Treap helper operations (static for clarity)
    # -----------------------------------------------------------------

    @staticmethod
    def _update(node: Node) -> None:
        """Recalc subtree aggregates after structural changes."""
        if node is None:
            return
        node.sub_sum = node.length
        node.sub_max_r = node.r
        if node.left:
            node.sub_sum += node.left.sub_sum
            node.sub_max_r = max(node.sub_max_r, node.left.sub_max_r)
        if node.right:
            node.sub_sum += node.right.sub_sum
            node.sub_max_r = max(node.sub_max_r, node.right.sub_max_r)

    @staticmethod
    def _split(root: Node, key: int) -> tuple[Node, Node]:
        """
        Split treap by key: left part contains all nodes with node.l < key,
        right part contains the rest.
        Returns (left_tree, right_tree).
        """
        if root is None:
            return (None, None)
        if root.l < key:
            # root and its left subtree all have l < key,
            # only right subtree might need splitting
            left, right = CountIntervals._split(root.right, key)
            root.right = left
            CountIntervals._update(root)
            return (root, right)
        else:
            left, right = CountIntervals._split(root.left, key)
            root.left = right
            CountIntervals._update(root)
            return (left, root)

    @staticmethod
    def _merge(left: Node, right: Node) -> Node:
        """
        Merge two treaps where all keys in left are smaller than all keys
        in right. Returns the merged root.
        """
        if left is None or right is None:
            return left or right
        if left.prio > right.prio:
            left.right = CountIntervals._merge(left.right, right)
            CountIntervals._update(left)
            return left
        else:
            right.left = CountIntervals._merge(left, right.left)
            CountIntervals._update(right)
            return right

    @staticmethod
    def _delete_node(root: Node, l: int) -> Node:
        """Delete the node with key `l` from the treap (assumes existence)."""
        if root is None:
            return None
        if l < root.l:
            root.left = CountIntervals._delete_node(root.left, l)
            CountIntervals._update(root)
            return root
        elif l > root.l:
            root.right = CountIntervals._delete_node(root.right, l)
            CountIntervals._update(root)
            return root
        else:
            # found target: merge its two children
            return CountIntervals._merge(root.left, root.right)

    @staticmethod
    def _max_node(root: Node) -> Node:
        """Return the node with the largest key in the treap."""
        if root is None:
            return None
        while root.right:
            root = root.right
        return root

    # -----------------------------------------------------------------
    #  Public API
    # -----------------------------------------------------------------

    def add(self, left: int, right: int) -> None:
        """
        Add the interval [left, right]. Merge it with any existing
        overlapping intervals and update the total count.
        """
        new_l = left
        new_r = right

        # 1) Split by left: L – intervals starting strictly before left.
        L, R = self._split(self.root, left)

        # Check the rightmost interval in L: it can overlap if its end >= left.
        # Because intervals are disjoint and sorted, at most one such interval exists.
        max_in_L = self._max_node(L)
        if max_in_L is not None and max_in_L.r >= left:
            new_l = min(new_l, max_in_L.l)
            new_r = max(new_r, max_in_L.r)
            self.total -= max_in_L.length
            L = self._delete_node(L, max_in_L.l)

        # 2) Split the rest (R) to isolate intervals that are completely
        #    covered by the merged range (start <= new_r).
        M, R2 = self._split(R, new_r + 1)   # M: all intervals with l <= new_r

        if M is not None:
            # All intervals in M overlap with the new interval – remove them.
            self.total -= M.sub_sum
            new_r = max(new_r, M.sub_max_r)
            # M is discarded entirely (not merged back)

        # 3) Create the new merged node and attach it.
        new_node = self.Node(new_l, new_r)
        self.total += new_node.length

        temp = self._merge(L, new_node)
        self.root = self._merge(temp, R2)

    def count(self) -> int:
        """Return the total number of integers covered by at least one interval."""
        return self.total