from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        # Build adjacency list representation of the graph
        n = len(passingFees)
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # State: (cost, time_used, current_city)
        # We use cost as the first element for min-heap priority
        pq = [(passingFees[0], 0, 0)]
        
        # Track the minimum time to reach each city with each possible cost
        # min_time[city][time] = minimum cost to reach city using exactly 'time' minutes
        # However, we need to track: for each city, what's the best (cost, time) pair we've seen
        # We'll use a different approach: track minimum cost for each (city, time) state
        # But since time can be up to 1000, we use a 2D array
        
        # min_cost[city][time] = minimum cost to reach city using at most 'time' minutes
        # This would require too much memory. Instead, we track visited states more carefully.
        
        # For each city, track the minimum time needed to reach it with a given cost
        # Or better: track all Pareto-optimal (time, cost) pairs for each city
        # A state (t1, c1) dominates (t2, c2) if t1 <= t2 and c1 <= c2
        
        # Simple approach: track minimum cost to reach each city at each time point
        min_cost = [[float('inf')] * (maxTime + 1) for _ in range(n)]
        min_cost[0][0] = passingFees[0]
        
        while pq:
            cost, time, city = heapq.heappop(pq)
            
            # If we've reached the destination, return the cost
            if city == n - 1:
                return cost
            
            # Skip if we've found a better path to this state already
            if cost > min_cost[city][time]:
                continue
            
            # Explore neighbors
            for neighbor, travel_time in graph[city]:
                new_time = time + travel_time
                new_cost = cost + passingFees[neighbor]
                
                # Check if within time limit
                if new_time <= maxTime:
                    # Only proceed if this is a better (lower cost) way to reach neighbor at new_time
                    # Also check if this state is worthwhile (not dominated by existing states)
                    if new_cost < min_cost[neighbor][new_time]:
                        # Update all time slots from new_time to maxTime if this cost is better
                        # This optimization helps prune dominated states
                        should_add = False
                        for t in range(new_time, maxTime + 1):
                            if new_cost < min_cost[neighbor][t]:
                                min_cost[neighbor][t] = new_cost
                                should_add = True
                        
                        if should_add:
                            heapq.heappush(pq, (new_cost, new_time, neighbor))
        
        # If we couldn't reach destination within maxTime
        return -1