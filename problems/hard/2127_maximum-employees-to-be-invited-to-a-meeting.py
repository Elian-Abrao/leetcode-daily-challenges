from typing import List
from collections import deque

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)

        # ---------- 1. topological removal of non-cycle nodes ----------
        indegree = [0] * n
        for f in favorite:
            indegree[f] += 1

        q = deque([i for i in range(n) if indegree[i] == 0])
        # depth[i] = longest chain (number of nodes) that ends at i,
        # not counting i itself. Initially zero.
        depth = [0] * n

        while q:
            u = q.popleft()
            v = favorite[u]
            # A chain ending at v can be extended by (u's chain + u itself)
            depth[v] = max(depth[v], depth[u] + 1)
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

        # ---------- 2. process the remaining cycles ----------
        visited = [False] * n
        answer = 0

        for i in range(n):
            # indegree > 0 means the node is part of a cycle
            if indegree[i] > 0 and not visited[i]:
                # collect the entire cycle
                cur = i
                cycle_nodes = []
                while not visited[cur]:
                    visited[cur] = True
                    cycle_nodes.append(cur)
                    cur = favorite[cur]

                cycle_len = len(cycle_nodes)
                if cycle_len == 2:
                    # For a 2‑cycle we can attach the best chain to each node
                    a, b = cycle_nodes[0], cycle_nodes[1]
                    answer = max(answer, 2 + depth[a] + depth[b])
                else:
                    # Longer cycles cannot be extended with extra nodes
                    answer = max(answer, cycle_len)

        return answer