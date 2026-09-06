from typing import List
from collections import deque

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        total = m * n

        # Encode the matrix as a bitmask.
        # Bit (r * n + c) represents the value of mat[r][c].
        start = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c]:
                    start |= 1 << (r * n + c)

        # Precompute the effect of flipping each cell.
        # Flipping (r, c) toggles itself and all valid neighbors.
        deltas = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
        flip_masks = []
        for r in range(m):
            for c in range(n):
                mask = 0
                for dr, dc in deltas:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        mask |= 1 << (nr * n + nc)
                flip_masks.append(mask)

        # Already a zero matrix.
        if start == 0:
            return 0

        # BFS over all states. There are at most 2^(m*n) <= 512 states.
        dist = [-1] * (1 << total)
        dist[start] = 0
        q = deque([start])

        while q:
            state = q.popleft()
            next_dist = dist[state] + 1

            for mask in flip_masks:
                nxt = state ^ mask
                if dist[nxt] != -1:
                    continue
                if nxt == 0:
                    return next_dist
                dist[nxt] = next_dist
                q.append(nxt)

        return -1