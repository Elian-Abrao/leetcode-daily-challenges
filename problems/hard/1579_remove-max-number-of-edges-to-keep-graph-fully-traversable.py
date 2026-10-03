from __future__ import annotations

class DSU:
    """Disjoint Set Union with path compression and union by rank."""
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        # Path compression: point directly to root
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        # Union by rank; returns True if merged, False if already same set
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        # Attach smaller rank tree under larger rank
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True

    def is_connected(self) -> bool:
        # Check if all nodes belong to the same set
        root = self.find(0)
        return all(self.find(i) == root for i in range(1, len(self.parent)))


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        # Convert to 0-based indexing
        # DSU for both persons (common), and separate for Alice and Bob
        dsu_common = DSU(n)
        dsu_alice = DSU(n)
        dsu_bob = DSU(n)

        used = 0  # number of edges we actually keep

        # --- Process type 3 edges first (benefit both) ---
        # Only count an edge as used if it connects two components in the common DSU.
        # Then also apply it to Alice and Bob DSUs (they will also merge since starting fresh).
        for typ, u, v in edges:
            if typ == 3:
                u -= 1
                v -= 1
                if dsu_common.union(u, v):
                    used += 1
                    dsu_alice.union(u, v)
                    dsu_bob.union(u, v)

        # --- Process type 1 edges (Alice only) ---
        for typ, u, v in edges:
            if typ == 1:
                u -= 1
                v -= 1
                if dsu_alice.union(u, v):
                    used += 1

        # --- Process type 2 edges (Bob only) ---
        for typ, u, v in edges:
            if typ == 2:
                u -= 1
                v -= 1
                if dsu_bob.union(u, v):
                    used += 1

        # Check if both Alice and Bob can traverse the whole graph
        if not dsu_alice.is_connected() or not dsu_bob.is_connected():
            return -1

        # Maximum removable = total edges - edges we needed to keep
        return len(edges) - used