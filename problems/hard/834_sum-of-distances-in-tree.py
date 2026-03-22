from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # A single node has no distance to add.
        if n == 1:
            return [0]

        # Build the undirected tree.
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        parent = [-1] * n
        depth = [0] * n
        order = []

        # Iterative DFS avoids recursion-limit issues on deep trees.
        stack = [0]
        parent[0] = 0

        while stack:
            node = stack.pop()
            order.append(node)

            for neighbor in graph[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                depth[neighbor] = depth[node] + 1
                stack.append(neighbor)

        answer = [0] * n

        # For root 0, the total distance is just the sum of node depths.
        root_distance_sum = 0
        for d in depth:
            root_distance_sum += d
        answer[0] = root_distance_sum

        # subtree_size[node] counts how many nodes stay with `node`
        # when the edge to its parent is cut.
        subtree_size = [1] * n

        # Postorder accumulation: children contribute their subtree sizes upward.
        for node in reversed(order[1:]):
            subtree_size[parent[node]] += subtree_size[node]

        # Re-root DP:
        # Moving root from parent -> child:
        # - child's subtree becomes 1 step closer for subtree_size[child] nodes
        # - all other nodes become 1 step farther
        for node in order[1:]:
            p = parent[node]
            answer[node] = answer[p] + n - 2 * subtree_size[node]

        return answer