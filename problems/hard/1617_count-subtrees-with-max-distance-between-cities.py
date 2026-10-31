from collections import deque
from typing import List

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # ---------- build adjacency list (0‑indexed) ----------
        adj = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)

        # ---------- all‑pairs distances in the whole tree ----------
        INF = n + 1                     # larger than any possible distance
        dist = [[INF] * n for _ in range(n)]
        for s in range(n):
            dist[s][s] = 0
            q = deque([s])
            while q:
                cur = q.popleft()
                for nb in adj[cur]:
                    if dist[s][nb] == INF:
                        dist[s][nb] = dist[s][cur] + 1
                        q.append(nb)

        # result array for diameters 1 .. n-1 (index d-1)
        ans = [0] * (n - 1)

        # ---------- enumerate all non‑empty subsets ----------
        for mask in range(1, 1 << n):
            sz = mask.bit_count()
            if sz < 2:
                continue                # ignore single‑node subtrees

            # ----- check connectivity of the induced subgraph -----
            # find the first node in the mask (lowest set bit)
            start = (mask & -mask).bit_length() - 1
            visited = 0
            q = deque([start])
            visited |= 1 << start
            while q:
                cur = q.popleft()
                for nb in adj[cur]:
                    if (mask >> nb) & 1 and not (visited >> nb) & 1:
                        visited |= 1 << nb
                        q.append(nb)
            if visited != mask:
                continue                # disconnected → skip

            # ----- compute diameter (max pairwise distance) -----
            nodes = [i for i in range(n) if (mask >> i) & 1]
            maxd = 0
            for i in range(len(nodes)):
                a = nodes[i]
                for j in range(i + 1, len(nodes)):
                    b = nodes[j]
                    d = dist[a][b]
                    if d > maxd:
                        maxd = d
            # maxd ≥ 1 because the subset has at least 2 nodes and is connected
            ans[maxd - 1] += 1

        return ans