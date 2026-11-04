from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        # Build adjacency list (1-indexed for convenience)
        adj = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)  # undirected graph

        # color[i] = -1 means uncolored; otherwise 0 or 1 representing two groups
        color = [-1] * (n + 1)

        def bfs(start: int) -> bool:
            """Try to color the component containing 'start' using BFS.
               Returns True if the component is bipartite, else False."""
            queue = deque([start])
            color[start] = 0
            while queue:
                node = queue.popleft()
                cur_color = color[node]
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        # Assign opposite color and continue
                        color[neighbor] = cur_color ^ 1
                        queue.append(neighbor)
                    elif color[neighbor] == cur_color:
                        # Conflict: neighbor has same color as current node
                        return False
            return True

        # Check each uncolored node (handles disconnected graphs)
        for i in range(1, n + 1):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True