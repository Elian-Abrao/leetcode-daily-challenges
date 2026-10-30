from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        
        # Reverse adjacency: for each node, store its predecessors.
        rev = [[] for _ in range(n)]
        # out_degree[i] = number of outgoing edges from node i.
        out_degree = [0] * n

        # Build reverse graph and compute out-degrees.
        for u in range(n):
            for v in graph[u]:
                rev[v].append(u)
                out_degree[u] += 1

        # Start with all terminal nodes (out-degree == 0).
        q = deque([i for i in range(n) if out_degree[i] == 0])
        safe = [False] * n

        # Topological elimination in reverse direction.
        while q:
            u = q.popleft()
            safe[u] = True
            # For each predecessor, one outgoing edge now leads to a safe node.
            for prev in rev[u]:
                out_degree[prev] -= 1
                if out_degree[prev] == 0:
                    # All outgoing edges from 'prev' lead to safe nodes.
                    q.append(prev)

        # Collect all safe nodes in ascending order (already sorted by index).
        return [i for i in range(n) if safe[i]]