from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        # Special case: single couple that is reversed (1,0) needs 1 swap
        if n == 1:
            return 1 if row[0] == 1 and row[1] == 0 else 0

        # Positions of each person
        pos = [0] * (2 * n)
        for idx, person in enumerate(row):
            pos[person] = idx

        # Union-Find
        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # For each couple, union the seat pairs they occupy
        for couple_id in range(n):
            a = 2 * couple_id
            b = 2 * couple_id + 1
            seat_a = pos[a] // 2
            seat_b = pos[b] // 2
            union(seat_a, seat_b)

        # Number of connected components among seat pairs
        components = sum(1 for i in range(n) if find(i) == i)
        return n - components