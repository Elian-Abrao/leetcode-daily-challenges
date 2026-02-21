from __future__ import annotations

from typing import List
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        Compute the minimum number of edges needed to visit all nodes.
        We perform a multi-source BFS over (node, visited_mask) states.
        Each starting node i starts with only node i visited.
        We expand to neighbors, updating the visited mask with the neighbor.
        As soon as we visit all nodes (mask == all_visited), we return the distance.
        """
        n = len(graph)
        if n == 1:
            # Already visited all nodes when there's only one node
            return 0

        all_visited = (1 << n) - 1  # mask with all bits set for n nodes

        # dist[node][mask] = minimum distance to reach 'node' having visited nodes as in 'mask'
        dist = [[-1] * (1 << n) for _ in range(n)]
        q = deque()

        # Initialize BFS with starting positions: each node individually
        for i in range(n):
            init_mask = 1 << i
            dist[i][init_mask] = 0
            q.append((i, init_mask))

        # Standard BFS over state space
        while q:
            u, mask = q.popleft()
            if mask == all_visited:
                # All nodes visited; current distance is optimal due to BFS
                return dist[u][mask]

            current_dist = dist[u][mask]
            # Explore all neighbors; update mask to include neighbor
            for v in graph[u]:
                next_mask = mask | (1 << v)
                if dist[v][next_mask] == -1:
                    dist[v][next_mask] = current_dist + 1
                    q.append((v, next_mask))

        # The graph is guaranteed to be connected; this return is just a safety net
        return -1