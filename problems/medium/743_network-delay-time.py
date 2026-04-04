from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list for the directed graph.
        graph = [[] for _ in range(n + 1)]
        for source, target, weight in times:
            graph[source].append((target, weight))

        # Dijkstra is optimal here because all edge weights are non-negative.
        distances = [float("inf")] * (n + 1)
        distances[k] = 0

        # Min-heap always expands the currently known shortest path first.
        min_heap = [(0, k)]

        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            # Ignore stale heap entries that were improved later.
            if current_time > distances[node]:
                continue

            # Relax outgoing edges from the current best-known node.
            for neighbor, travel_time in graph[node]:
                new_time = current_time + travel_time
                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        # Exclude index 0 because nodes are 1-indexed.
        max_time = max(distances[1:])

        # If any node stayed unreachable, the signal cannot reach everyone.
        return -1 if max_time == float("inf") else max_time