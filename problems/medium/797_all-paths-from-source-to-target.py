from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        target = n - 1
        result = []  # will hold all valid paths
        
        # DFS backtracking: path is the current list of nodes visited
        def backtrack(node: int, path: List[int]) -> None:
            # Append current node to the path
            path.append(node)
            
            # If we reached the target, record a copy of the path
            if node == target:
                result.append(path[:])  # deep copy
            else:
                # Explore all neighbors (DAG ensures no cycles)
                for neighbor in graph[node]:
                    backtrack(neighbor, path)
            
            # Backtrack: remove current node to explore other branches
            path.pop()
        
        # Start the traversal from node 0
        backtrack(0, [])
        return result