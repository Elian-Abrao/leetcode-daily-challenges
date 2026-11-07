from collections import deque
from typing import List

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**9  # larger than any possible time (max cells 20000)

        # ---- 1. compute fire arrival time for every cell ----
        fire_time = [[INF] * n for _ in range(m)]
        q = deque()
        # initialise with all fire cells
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:          # initial fire
                    fire_time[r][c] = 0
                    q.append((r, c))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            next_time = fire_time[r][c] + 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2:
                    if next_time < fire_time[nr][nc]:
                        fire_time[nr][nc] = next_time
                        q.append((nr, nc))

        # ---- 2. check the special case of a forever-safe path ----
        # If there exists a path that uses only cells never reached by fire,
        # then we can wait arbitrarily long and still succeed.
        if self._exists_fireproof_path(grid, fire_time, m, n):
            return 10**9

        # ---- 3. binary search on waiting time ----
        # The maximum minutes we could possibly wait is limited.
        # If start is reachable by fire, waiting more than fire_time[0][0]-1
        # burns the start.  Otherwise the bound is the total number of cells
        # (since after that fire has covered everything reachable).
        upper_bound = m * n
        if fire_time[0][0] != INF:
            upper_bound = min(upper_bound, fire_time[0][0] - 1)

        # helper function to test feasibility for a given waiting time
        def can_reach(wait: int) -> bool:
            if wait >= fire_time[0][0]:
                return False               # start already on fire
            visited = [[False] * n for _ in range(m)]
            q = deque()
            q.append((0, 0))
            visited[0][0] = True
            step = 0                       # moves performed so far
            while q:
                # process all cells at the current move distance
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if r == m - 1 and c == n - 1:
                        return True        # reached safehouse
                    arrival = wait + step + 1   # time after moving to neighbour
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 2:
                            # safehouse allows arrival <= fire time, others strictly <
                            if nr == m - 1 and nc == n - 1:
                                if arrival <= fire_time[nr][nc]:
                                    visited[nr][nc] = True
                                    q.append((nr, nc))
                            else:
                                if arrival < fire_time[nr][nc]:
                                    visited[nr][nc] = True
                                    q.append((nr, nc))
                step += 1
            return False

        lo, hi = 0, upper_bound
        best = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_reach(mid):
                best = mid            # feasible, try larger wait
                lo = mid + 1
            else:
                hi = mid - 1
        return best

    # ------------------------------------------------------------
    def _exists_fireproof_path(self, grid: List[List[int]],
                               fire_time: List[List[int]],
                               m: int, n: int) -> bool:
        """BFS from (0,0) restricted to cells where fire never arrives."""
        if fire_time[0][0] != 10**9:   # start will burn eventually
            return False
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = [[False] * n for _ in range(m)]
        q = deque()
        q.append((0, 0))
        visited[0][0] = True
        while q:
            r, c = q.popleft()
            if r == m - 1 and c == n - 1:
                return True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 2:
                    # only move onto cells that fire will never touch
                    if fire_time[nr][nc] == 10**9:
                        visited[nr][nc] = True
                        q.append((nr, nc))
        return False