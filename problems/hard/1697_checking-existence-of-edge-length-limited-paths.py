from typing import List

class UnionFind:
    """Union-Find (Disjoint Set Union) with path compression and union by size."""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n  # arbitrary initial size
    
    def find(self, x: int) -> int:
        # Path compression: make root point directly to grandparent
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        # Union by size: attach smaller tree under larger tree
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
    
    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], 
                                   queries: List[List[int]]) -> List[bool]:
        # Sort edges by distance (ascending)
        edges_sorted = sorted(edgeList, key=lambda e: e[2])
        
        # Attach original index to each query and sort by limit
        queries_with_idx = [(q[0], q[1], q[2], i) for i, q in enumerate(queries)]
        queries_sorted = sorted(queries_with_idx, key=lambda x: x[2])
        
        uf = UnionFind(n)
        ans = [False] * len(queries)
        edge_ptr = 0  # pointer into edges_sorted
        
        # Process queries in order of increasing limit
        for p, q, limit, idx in queries_sorted:
            # Add all edges with distance strictly less than current limit
            while edge_ptr < len(edges_sorted) and edges_sorted[edge_ptr][2] < limit:
                u, v, _ = edges_sorted[edge_ptr]
                uf.union(u, v)
                edge_ptr += 1
            # After adding eligible edges, check connectivity
            ans[idx] = uf.connected(p, q)
        
        return ans