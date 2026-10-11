from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # -1 = uncolored, 0 and 1 are the two colors
        color = [-1] * n

        # The graph may be disconnected, so check every component
        for start in range(n):
            if color[start] != -1:
                # Already colored in a previous component
                continue

            # Start a new BFS from this node, coloring it with 0
            color[start] = 0
            queue = deque([start])

            while queue:
                node = queue.popleft()
                current_color = color[node]
                neighbor_color = 1 - current_color  # opposite color

                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        # Assign the opposite color and enqueue
                        color[neighbor] = neighbor_color
                        queue.append(neighbor)
                    elif color[neighbor] != neighbor_color:
                        # Conflict: neighbor has the same color as current node
                        return False

        return True