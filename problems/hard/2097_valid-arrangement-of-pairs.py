from typing import List
from collections import defaultdict, deque

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # This problem is finding an Eulerian path in a directed graph
        # where each pair [u, v] represents a directed edge from u to v
        
        # Build adjacency list (graph) and track in/out degrees
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        # Find the starting node for Eulerian path
        # In an Eulerian path:
        # - Start node has out_degree - in_degree = 1
        # - End node has in_degree - out_degree = 1
        # - All other nodes have in_degree = out_degree
        # If all nodes are balanced, we can start from any node (Eulerian circuit)
        
        start_node = pairs[0][0]  # Default to any node
        
        # Look for a node with out_degree > in_degree (must be start of path)
        for node in out_degree:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break
        
        # Use Hierholzer's algorithm to find Eulerian path
        # We'll use iterative DFS with a stack
        stack = [start_node]
        path = []
        
        while stack:
            curr = stack[-1]
            if graph[curr]:
                # Follow an edge
                next_node = graph[curr].popleft()
                stack.append(next_node)
            else:
                # No more edges from current node, add to path
                path.append(stack.pop())
        
        # Path is built in reverse order
        path.reverse()
        
        # Convert node path to edge pairs
        # path contains nodes, we need to reconstruct [start, end] pairs
        result = []
        for i in range(len(path) - 1):
            result.append([path[i], path[i + 1]])
        
        return result