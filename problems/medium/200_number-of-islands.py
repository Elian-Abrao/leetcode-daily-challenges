from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Guard against malformed input, even though LeetCode guarantees dimensions.
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for row in range(rows):
            for col in range(cols):
                # Only unvisited land can start a new island.
                if grid[row][col] != "1":
                    continue

                islands += 1

                # Iterative DFS avoids recursion depth issues on large dense grids.
                stack = [(row, col)]
                grid[row][col] = "0"  # Mark immediately to avoid duplicate pushes.

                while stack:
                    current_row, current_col = stack.pop()

                    # Explore the four orthogonal neighbors; diagonals do not connect islands.
                    if current_row > 0 and grid[current_row - 1][current_col] == "1":
                        grid[current_row - 1][current_col] = "0"
                        stack.append((current_row - 1, current_col))

                    if current_row + 1 < rows and grid[current_row + 1][current_col] == "1":
                        grid[current_row + 1][current_col] = "0"
                        stack.append((current_row + 1, current_col))

                    if current_col > 0 and grid[current_row][current_col - 1] == "1":
                        grid[current_row][current_col - 1] = "0"
                        stack.append((current_row, current_col - 1))

                    if current_col + 1 < cols and grid[current_row][current_col + 1] == "1":
                        grid[current_row][current_col + 1] = "0"
                        stack.append((current_row, current_col + 1))

        return islands