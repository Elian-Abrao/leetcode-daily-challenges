import collections
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        """
        Simulate the containment process day by day.
        Each day:
          1. Find all connected components of infected cells (value == 1).
          2. For each component compute:
               - threat_count : number of distinct uninfected cells adjacent to it.
               - walls_needed  : number of edges between the component and uninfected cells.
          3. Pick the component with the largest threat_count (ties never occur).
          4. Build walls around it (add walls_needed to the answer) and mark its cells as
             contained (value == 2, inert).
          5. Let the virus spread from every remaining active infected cell (value == 1)
             to all adjacent uninfected cells (value == 0) simultaneously.
        Repeat until no active infected cells remain or no component threatens any
        uninfected cell (world fully infected or fully contained).
        """
        grid = isInfected
        m, n = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        total_walls = 0

        while True:
            # ----- Step 1: find all infected components (value == 1) -----
            visited = [[False] * n for _ in range(m)]
            components = []          # each: (list_of_cells, walls_needed, threat_count)

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        # BFS for this component
                        q = collections.deque()
                        q.append((i, j))
                        visited[i][j] = True
                        cells = []          # all cells of the component
                        walls = 0           # perimeter to uninfected cells
                        threats = set()     # distinct uninfected neighbours

                        while q:
                            x, y = q.popleft()
                            cells.append((x, y))
                            for dx, dy in DIRS:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n:
                                    if grid[nx][ny] == 0:
                                        walls += 1
                                        threats.add((nx, ny))
                                    elif grid[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = True
                                        q.append((nx, ny))
                        components.append((cells, walls, len(threats)))

            # No active infected cells left → done
            if not components:
                break

            # ----- Step 2: select component with the largest threat_count -----
            best_idx = 0
            best_threat = -1
            for idx, (_, _, threat) in enumerate(components):
                if threat > best_threat:
                    best_threat = threat
                    best_idx = idx

            # No component threatens any uninfected cell → stop (fully infected/isolated)
            if best_threat == 0:
                break

            # ----- Step 3: quarantine the selected component -----
            cells_to_contain, walls_needed, _ = components[best_idx]
            total_walls += walls_needed
            for x, y in cells_to_contain:
                grid[x][y] = 2          # 2 = contained (inert)

            # ----- Step 4: virus spread overnight (simultaneous) -----
            new_infections = set()
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:          # active infected
                        for dx, dy in DIRS:
                            ni, nj = i + dx, j + dy
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                                new_infections.add((ni, nj))
            # Apply all new infections at once
            for x, y in new_infections:
                grid[x][y] = 1

        return total_walls