from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        # Track the first parent seen for each node.
        # If a node gets a second parent, we must choose between those two edges.
        parent = list(range(n + 1))
        first_candidate = None
        second_candidate = None

        for u, v in edges:
            if parent[v] != v:
                # v already has a parent, so these are the only two edges
                # that can possibly be removed in the "two parents" scenario.
                first_candidate = [parent[v], v]
                second_candidate = [u, v]
            else:
                parent[v] = u

        # Union-Find detects whether the remaining edges still create a cycle.
        uf_parent = list(range(n + 1))
        uf_rank = [0] * (n + 1)

        def find(x: int) -> int:
            # Path compression keeps the amortized cost almost constant.
            while uf_parent[x] != x:
                uf_parent[x] = uf_parent[uf_parent[x]]
                x = uf_parent[x]
            return x

        def union(a: int, b: int) -> bool:
            # Return False when a and b are already connected,
            # which means adding this directed edge closes a cycle.
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False

            # Union by rank avoids tall trees in the DSU structure.
            if uf_rank[root_a] < uf_rank[root_b]:
                uf_parent[root_a] = root_b
            elif uf_rank[root_a] > uf_rank[root_b]:
                uf_parent[root_b] = root_a
            else:
                uf_parent[root_b] = root_a
                uf_rank[root_a] += 1
            return True

        for u, v in edges:
            # In the two-parents case, temporarily ignore the later edge.
            # If the rest forms a valid tree, this later edge is the answer.
            if second_candidate is not None and u == second_candidate[0] and v == second_candidate[1]:
                continue

            if not union(u, v):
                # If no node has two parents, the redundant edge is exactly
                # the one that creates the directed cycle.
                if first_candidate is None:
                    return [u, v]

                # Otherwise, skipping the later conflicting edge still leaves a cycle,
                # so the earlier conflicting edge must be part of that cycle.
                return first_candidate

        # If no cycle appears after skipping the later conflicting edge,
        # removing that later edge restores a rooted tree.
        return second_candidate if second_candidate is not None else []