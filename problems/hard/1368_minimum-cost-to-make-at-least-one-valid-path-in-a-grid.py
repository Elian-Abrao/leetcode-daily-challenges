from collections import deque

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # movement vectors for direction indices 1..4
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        INF = 10 ** 9
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque()
        dq.append((0, 0))

        while dq:
            i, j = dq.popleft()
            # first time we pop the destination its distance is optimal
            if i == m - 1 and j == n - 1:
                return dist[i][j]

            for idx, (dx, dy) in enumerate(dirs, start=1):
                ni, nj = i + dx, j + dy
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                # cost = 0 if original arrow points this way, else 1 (modify)
                cost = 0 if grid[i][j] == idx else 1
                nd = dist[i][j] + cost
                if nd < dist[ni][nj]:
                    dist[ni][nj] = nd
                    if cost == 0:
                        dq.appendleft((ni, nj))   # zero-weight edge to front
                    else:
                        dq.append((ni, nj))       # one-weight edge to back

        # theoretically unreachable because a path always exists
        return dist[m - 1][n - 1]