from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Bellman-Ford style DP: we compute the minimum cost to reach each city
        using at most 'k' stops (i.e., at most k+1 edges).
        """
        # Large sentinel value (sum of all edge weights cannot exceed 1e6, so 1e9 is safe)
        INF = 10**9

        # dist[city] = cheapest price to reach city after a certain number of stops
        # Initialize: only source is reachable with cost 0 and 0 stops used
        dist = [INF] * n
        dist[src] = 0

        # Perform k+1 iterations:
        # after i-th iteration, dist holds min cost using at most i edges (stops)
        for _ in range(k + 1):
            # new_dist copies the previous iteration's results;
            # we only update based on the previous iteration's distances to avoid
            # using more edges than allowed in the current iteration.
            new_dist = dist[:]   # shallow copy of list
            for u, v, w in flights:
                # if we can reach u with the previous number of stops,
                # then we can reach v with one more stop (current iteration)
                if dist[u] != INF and dist[u] + w < new_dist[v]:
                    new_dist[v] = dist[u] + w
            dist = new_dist

        # After k+1 iterations, dist[dst] holds the minimum cost using ≤k stops
        return dist[dst] if dist[dst] != INF else -1