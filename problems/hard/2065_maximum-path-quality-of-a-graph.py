from typing import List

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # Build adjacency list for the graph
        n = len(values)
        graph = [[] for _ in range(n)]
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Track the maximum quality found
        max_quality = [0]
        
        # Track visit count for each node to calculate quality correctly
        # (only count value once even if visited multiple times)
        visit_count = [0] * n
        
        def dfs(node: int, time_spent: int, current_quality: int) -> None:
            """
            DFS to explore all valid paths starting from node 0 and returning to node 0.
            
            Args:
                node: current node being visited
                time_spent: total time spent so far
                current_quality: sum of unique node values visited so far
            """
            # If we're back at node 0, update max quality
            # We can only count paths that end at node 0
            if node == 0:
                max_quality[0] = max(max_quality[0], current_quality)
            
            # Explore all neighbors
            for neighbor, travel_time in graph[node]:
                new_time = time_spent + travel_time
                
                # Prune: if we exceed maxTime, don't explore this path
                if new_time > maxTime:
                    continue
                
                # Check if this is the first visit to the neighbor
                is_first_visit = (visit_count[neighbor] == 0)
                
                # Mark neighbor as visited
                visit_count[neighbor] += 1
                
                # Add neighbor's value only if it's the first visit
                new_quality = current_quality + (values[neighbor] if is_first_visit else 0)
                
                # Recursively explore from neighbor
                dfs(neighbor, new_time, new_quality)
                
                # Backtrack: unmark the visit
                visit_count[neighbor] -= 1
        
        # Start DFS from node 0 with time 0
        # Mark node 0 as visited and add its value to quality
        visit_count[0] = 1
        dfs(0, 0, values[0])
        
        return max_quality[0]