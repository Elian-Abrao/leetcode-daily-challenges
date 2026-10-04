class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        """
        Count all paths from start to end that visit every non-obstacle cell exactly once.
        Uses DFS with backtracking, modifying the grid to mark visited cells.
        """
        m, n = len(grid), len(grid[0])
        
        # Locate start cell and count total number of walkable cells.
        start_r = start_c = 0
        total_walkable = 0  # cells that are not obstacles (0, 1, 2)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                    total_walkable += 1
                elif grid[r][c] == 2:
                    total_walkable += 1
                elif grid[r][c] == 0:
                    total_walkable += 1
                # -1 is obstacle, ignore.
        
        # Direction vectors: right, down, left, up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(r: int, c: int, visited: int) -> int:
            """
            Explore from (r,c). visited counts how many walkable cells have been
            visited so far (including the current cell).
            """
            # If we reached the end, check if we have visited all walkable cells.
            if grid[r][c] == 2:
                return 1 if visited == total_walkable else 0
            
            # Mark current cell as visited by setting to a sentinel value.
            original = grid[r][c]
            grid[r][c] = -2  # visited marker (not obstacle, not walkable)
            
            paths = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    # Only step onto unvisited walkable cells (0 or 2).
                    if grid[nr][nc] != -1 and grid[nr][nc] != -2:
                        paths += dfs(nr, nc, visited + 1)
            
            # Backtrack: restore original cell value.
            grid[r][c] = original
            return paths
        
        # Start DFS with the start cell already counted as visited.
        return dfs(start_r, start_c, 1)