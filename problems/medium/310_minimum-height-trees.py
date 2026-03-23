from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # A single node is trivially the unique centroid and root of the MHT.
        if n == 1:
            return [0]

        # Build the adjacency list and track degrees so we can peel leaves layer by layer.
        graph = [[] for _ in range(n)]
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        # Initial leaves are exactly the nodes with one neighbor.
        leaves = deque(node for node in range(n) if degree[node] == 1)
        remaining_nodes = n

        # Repeatedly remove the current outer layer.
        # The last one or two nodes left are the tree centroids, which minimize height.
        while remaining_nodes > 2:
            layer_size = len(leaves)
            remaining_nodes -= layer_size

            for _ in range(layer_size):
                leaf = leaves.popleft()

                # Each leaf has at most one still-active neighbor in the pruned tree.
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1

                    # A node becomes a new leaf exactly when only one active edge remains.
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        # A tree has either one centroid or two adjacent centroids.
        return list(leaves)