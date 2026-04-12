from typing import List
from heapq import heappush, heappop

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # Build adjacency list for the original graph.
        # For each edge, store (neighbor, weight, cnt) where:
        # - weight = cnt + 1 (number of steps to traverse this subdivided edge)
        # - cnt    = number of new subdivided nodes on this edge
        adj = [[] for _ in range(n)]
        for u, v, cnt in edges:
            w = cnt + 1
            adj[u].append((v, w, cnt))
            adj[v].append((u, w, cnt))

        # Dijkstra from node 0 to compute minimum distance to every original node.
        INF = 10**18
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]  # (distance, node)

        while pq:
            d, u = heappop(pq)
            if d != dist[u]:
                continue  # stale entry
            for v, w, cnt in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(pq, (nd, v))

        # Count reachable original nodes (distance to them <= maxMoves)
        reachable_original = sum(1 for d in dist if d <= maxMoves)

        # Count reachable subdivided nodes along each edge.
        # For edge (u, v, cnt), compute how many subdivided nodes are reachable
        # from u-side and v-side, then take the union (no double counting).
        reachable_subdivided = 0
        for u, v, cnt in edges:
            rem_u = max(0, maxMoves - dist[u])
            rem_v = max(0, maxMoves - dist[v])
            a = min(cnt, rem_u)
            b = min(cnt, rem_v)
            reachable_subdivided += min(a + b, cnt)

        return reachable_original + reachable_subdivided

if __name__ == "__main__":
    pass