from __future__ import annotations

class UnionFind:
    """
    Disjoint Set Union with path compression and union by rank.
    Tracks connected components for an array of size n.
    """
    __slots__ = ("parent", "rank")

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        # Path compression: make every node point directly to the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        # Attach the smaller tree under the larger tree
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1


class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        # Each cell is divided into 4 triangles:
        # 0 = top, 1 = right, 2 = bottom, 3 = left
        total_triangles = 4 * n * n
        uf = UnionFind(total_triangles)

        for i in range(n):
            for j in range(n):
                # Base index for the four triangles in cell (i, j)
                base = 4 * (i * n + j)
                ch = grid[i][j]

                # Internal connections determined by the character
                if ch == ' ':
                    # Space: all 4 triangles are connected
                    uf.union(base + 0, base + 1)
                    uf.union(base + 1, base + 2)
                    uf.union(base + 2, base + 3)
                elif ch == '/':
                    # '/' connects top-left (0-3) and bottom-right (1-2)
                    uf.union(base + 0, base + 3)
                    uf.union(base + 1, base + 2)
                else:  # ch == '\\'
                    # '\' connects top-right (0-1) and bottom-left (3-2)
                    uf.union(base + 0, base + 1)
                    uf.union(base + 3, base + 2)

                # External connections with the right neighbor
                if j + 1 < n:
                    # Right triangle of current cell (1) with left triangle of right cell (3)
                    right_base = 4 * (i * n + (j + 1))
                    uf.union(base + 1, right_base + 3)

                # External connections with the bottom neighbor
                if i + 1 < n:
                    # Bottom triangle of current cell (2) with top triangle of below cell (0)
                    below_base = 4 * ((i + 1) * n + j)
                    uf.union(base + 2, below_base + 0)

        # Count distinct connected components (roots)
        roots = set()
        for t in range(total_triangles):
            roots.add(uf.find(t))

        return len(roots)