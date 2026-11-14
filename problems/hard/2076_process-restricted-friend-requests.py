class Solution:
    def friendRequests(self, n: int, restrictions: list[list[int]], requests: list[list[int]]) -> list[bool]:
        # Union-Find with path compression and union by rank
        parent = list(range(n))
        rank = [0] * n
        
        def find(x: int) -> int:
            # Path compression: set parent to root
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x: int, y: int) -> None:
            # Union by rank: attach smaller tree under larger
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
        
        # Pre-compute the root pairs for each restriction for fast lookup
        # We'll re-check each restriction during every request
        result = []
        
        for u, v in requests:
            # Already friends? Then always successful
            if find(u) == find(v):
                result.append(True)
                continue
            
            # Temporarily union to check if any restriction is violated
            # Save original state to roll back if needed
            # Since n <= 1000, we can simulate by storing roots before union attempt
            ru, rv = find(u), find(v)
            
            # Try to add the edge, check all restrictions
            # To check if adding edge (u,v) would connect two groups that violate a restriction:
            # We need to see if there exists a restriction (a,b) such that:
            # - a and b are currently in different groups
            # - after merging ru and rv, they would become connected
            # That happens exactly when (find(a), find(b)) == (ru, rv) or (rv, ru)
            
            possible = True
            for a, b in restrictions:
                ra, rb = find(a), find(b)
                # Check if merging ru and rv would connect ra and rb
                # This occurs when one of ra,rb is ru and the other is rv
                if (ra == ru and rb == rv) or (ra == rv and rb == ru):
                    possible = False
                    break
            
            if possible:
                # Actually perform the union
                union(u, v)
                result.append(True)
            else:
                result.append(False)
        
        return result