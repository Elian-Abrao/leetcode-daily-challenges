from typing import List

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # For each vertex, store up to 3 neighbors with highest scores.
        # We only need the node ids; score can be retrieved from scores[].
        best_neighbors = [[] for _ in range(n)]
        for u in range(n):
            # Collect all neighbors with their scores, sort descending, keep top 3
            neigh_with_score = [(scores[v], v) for v in adj[u]]
            neigh_with_score.sort(reverse=True)
            # Keep only node ids (we already have scores array)
            best_neighbors[u] = [v for _, v in neigh_with_score[:3]]

        ans = -1

        # Try every edge as the middle edge of the 4-node path.
        for u, v in edges:
            # For each candidate on the u side (neighbor of u, not v)
            for a in best_neighbors[u]:
                if a == v:
                    continue
                for b in best_neighbors[v]:
                    if b == u:
                        continue
                    if a == b:
                        continue  # nodes must be distinct
                    # Form path a - u - v - b
                    total = scores[a] + scores[u] + scores[v] + scores[b]
                    if total > ans:
                        ans = total

        return ans