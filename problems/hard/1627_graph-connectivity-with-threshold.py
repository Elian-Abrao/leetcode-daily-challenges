class Solution:
    def areConnected(self, n: int, threshold: int, queries: list[list[int]]) -> list[bool]:
        """
        Build a DSU (Union-Find) connecting cities that share a common divisor > threshold.
        For each divisor d from threshold+1 to n, union d with every multiple of d.
        Then answer connectivity queries in near-constant time.
        """
        # ---------- DSU implementation ----------
        parent = list(range(n + 1))   # 1-indexed, parent[0] unused
        size = [1] * (n + 1)

        def find(x: int) -> int:
            # Path compression (iterative with halving)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # Attach smaller tree under larger tree (union by size)
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # ---------- Build components ----------
        # For every possible divisor d greater than threshold,
        # union all multiples of d. This connects any two numbers
        # that share d as a common divisor.
        for d in range(threshold + 1, n + 1):
            # Start from d and step by d: union(d, multiple)
            # union(d, d) is a no-op but harmless
            for multiple in range(d, n + 1, d):
                union(d, multiple)

        # ---------- Answer queries ----------
        return [find(a) == find(b) for a, b in queries]