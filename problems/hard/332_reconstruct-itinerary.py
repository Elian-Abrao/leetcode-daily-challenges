from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build adjacency list: each airport maps to a sorted list of destinations
        # Using defaultdict with list for convenience
        graph = defaultdict(list)
        
        # Sort tickets to ensure lexical order when we process destinations
        # We need to visit destinations in reverse sorted order because we'll pop from end
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        
        # Result will store the final itinerary in reverse order initially
        result = []
        
        # Hierholzer's algorithm for finding Eulerian path
        # Use iterative DFS with explicit stack to avoid potential stack overflow
        stack = ["JFK"]
        
        while stack:
            curr = stack[-1]
            
            # If current airport has outgoing edges, continue traversal
            if graph[curr]:
                # Pop the last (lexicographically smallest due to reverse sort) destination
                next_dest = graph[curr].pop()
                stack.append(next_dest)
            else:
                # No more outgoing edges: this node is part of the final path
                # Add to result (we're building the path in reverse)
                result.append(stack.pop())
        
        # The result is built in reverse order (postorder), so reverse it
        return result[::-1]