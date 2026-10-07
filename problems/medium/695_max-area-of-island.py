class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        Returns the maximum area of a 4-directionally connected island of 1's.
        Uses iterative DFS (stack) to avoid recursion depth issues.
        Marks visited cells by setting them to 0 (in-place) to save memory.
        """
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        # 4-directional neighbors: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Start a new island discovery using stack
                    stack = [(r, c)]
                    grid[r][c] = 0  # mark visited
                    current_area = 0

                    while stack:
                        x, y = stack.pop()
                        current_area += 1

                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            # Check bounds and land
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                                grid[nx][ny] = 0  # mark immediately to avoid revisit
                                stack.append((nx, ny))

                    # Update max area
                    if current_area > max_area:
                        max_area = current_area

        return max_area