from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        
        # Build adjacency list for the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Precompute coprime pairs - since nums[i] <= 50, we only need to check values 1-50
        # coprime_map[val] = list of values coprime with val
        coprime_map = defaultdict(list)
        for i in range(1, 51):
            for j in range(1, 51):
                if gcd(i, j) == 1:
                    coprime_map[i].append(j)
        
        result = [-1] * n
        
        # For each possible value (1-50), track the stack of (node_index, depth) pairs
        # seen along the current path from root to current node
        # This allows us to quickly find the closest ancestor with a coprime value
        value_stack = [[] for _ in range(51)]
        
        def dfs(node, parent, depth):
            current_val = nums[node]
            
            # Find the closest ancestor with a coprime value
            best_ancestor = -1
            best_depth = -1
            
            # Check all values that are coprime with current_val
            for coprime_val in coprime_map[current_val]:
                # If we have ancestors with this coprime value, pick the deepest (closest)
                if value_stack[coprime_val]:
                    ancestor_node, ancestor_depth = value_stack[coprime_val][-1]
                    if ancestor_depth > best_depth:
                        best_depth = ancestor_depth
                        best_ancestor = ancestor_node
            
            result[node] = best_ancestor
            
            # Add current node to the stack for its value
            value_stack[current_val].append((node, depth))
            
            # Visit children
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node, depth + 1)
            
            # Backtrack: remove current node from the stack
            value_stack[current_val].pop()
        
        # Start DFS from root (node 0) with depth 0
        dfs(0, -1, 0)
        
        return result