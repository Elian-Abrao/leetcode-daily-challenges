from typing import List
from collections import deque, defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        
        # Build adjacency list and compute in-degrees
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # dp[node][color] = max count of 'color' on any path ending at 'node'
        # We use 26 colors (a-z)
        dp = [[0] * 26 for _ in range(n)]
        
        # Initialize queue with all nodes having in-degree 0
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
                # Each node starts with count 1 for its own color
                dp[i][ord(colors[i]) - ord('a')] = 1
        
        processed_count = 0  # Count nodes processed to detect cycles
        max_color_value = 0
        
        # Topological sort with DP
        while queue:
            u = queue.popleft()
            processed_count += 1
            
            # Track the max color value at current node
            color_idx = ord(colors[u]) - ord('a')
            max_color_value = max(max_color_value, dp[u][color_idx])
            
            # Process all neighbors
            for v in graph[u]:
                # Update dp[v] by taking max from all incoming edges
                # For the color of node v itself, we add 1
                v_color_idx = ord(colors[v]) - ord('a')
                
                for c in range(26):
                    if c == v_color_idx:
                        # Inherit count from u and add 1 for node v
                        dp[v][c] = max(dp[v][c], dp[u][c] + 1)
                    else:
                        # Just inherit the count from u
                        dp[v][c] = max(dp[v][c], dp[u][c])
                
                # Reduce in-degree and add to queue if it becomes 0
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        # If not all nodes are processed, there's a cycle
        if processed_count != n:
            return -1
        
        return max_color_value