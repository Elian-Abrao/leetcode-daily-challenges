from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Count the number of provinces (connected components) in an undirected
        graph represented by its adjacency matrix.

        We use DFS to traverse each component and mark visited cities.
        Complexity: O(n^2) time, O(n) extra space for the visited array.
        """
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(city: int) -> None:
            """Mark all cities reachable from 'city' as visited."""
            visited[city] = True
            # Check all possible neighbors (adjacency matrix row)
            for neighbor in range(n):
                # If there's a direct edge and neighbor not yet visited
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        # Iterate over all cities; start a new DFS for each unvisited one.
        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)

        return provinces