from typing import List

class UnionFind:
    """Disjoint-set data structure with path compression and union by size."""

    def __init__(self, n: int):
        # Nodes are labelled 1..n, so allocate one extra slot for 1-indexing.
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x: int) -> int:
        """Return the root of the set containing x (with path compression)."""
        # Iterative path compression for efficiency.
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        """
        Merge the sets of a and b.
        Return True if the sets were different (successful union),
        False if they were already in the same set (edge would create a cycle).
        """
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                     # already connected -> cycle detected

        # Union by size: attach the smaller tree under the larger one.
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Return an edge that can be removed so that the resulting graph is a tree.
        If multiple answers exist, return the one that occurs last in the input.
        """
        n = len(edges)                       # graph has exactly n nodes (since n == edges.length)
        uf = UnionFind(n)

        for u, v in edges:
            if not uf.union(u, v):
                # This edge connects two nodes already in the same connected component,
                # therefore it completes a cycle. Because we process edges in order,
                # this is the last edge of the cycle in the input order.
                return [u, v]

        # Problem guarantees that a solution exists; this line is never reached.
        return []