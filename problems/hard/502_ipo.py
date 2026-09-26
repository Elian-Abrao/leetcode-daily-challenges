from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Pair each project's capital requirement with its profit
        projects = list(zip(capital, profits))
        # Sort by capital needed (ascending) so we can unlock projects gradually
        projects.sort(key=lambda x: x[0])

        # Max-heap implemented with negative values for profits
        max_heap = []
        i = 0
        n = len(projects)

        # At most k projects can be chosen
        for _ in range(k):
            # Add all projects whose capital requirement is <= current capital w
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            # If no project is affordable, we cannot proceed further
            if not max_heap:
                break
            # Take the most profitable available project
            w += -heapq.heappop(max_heap)

        return w