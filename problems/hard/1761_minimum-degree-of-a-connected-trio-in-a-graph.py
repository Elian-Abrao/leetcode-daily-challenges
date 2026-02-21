from typing import List

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency sets for O(1) neighbor checks
        adj = [set() for _ in range(n + 1)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        # Precompute degrees (total number of neighbors) for each node
        deg = [0] * (n + 1)
        for i in range(1, n + 1):
            deg[i] = len(adj[i])

        min_degree = float('inf')
        found = False

        # Iterate over edges and look for a common neighbor w to form a triangle (u, v, w)
        # To avoid counting the same triangle multiple times, enforce an order: u < v < w
        # For each edge (a, b), consider u = min(a,b), v = max(a,b)
        for a, b in edges:
            u, v = (a, b) if a < b else (b, a)

            # Iterate over the smaller of the two neighbor sets to minimize checks
            if len(adj[u]) <= len(adj[v]):
                smaller, other = adj[u], adj[v]
            else:
                smaller, other = adj[v], adj[u]

            # For any w in common neighbors, ensure the order u < v < w to count once
            for w in smaller:
                if w > v and w in other:
                    tri_deg = deg[u] + deg[v] + deg[w] - 6  # external edges to the trio
                    if tri_deg < min_degree:
                        min_degree = tri_deg
                    found = True

        return -1 if not found else int(min_degree)