class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        # Build the binary grid: 1 for valid cells, 0 for mines
        grid = [[1] * n for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0

        # Left arm length (including current cell)
        left = [[0] * n for _ in range(n)]
        for i in range(n):
            cnt = 0
            for j in range(n):
                cnt = cnt + 1 if grid[i][j] else 0
                left[i][j] = cnt

        # Right arm length (scanning from right)
        right = [[0] * n for _ in range(n)]
        for i in range(n):
            cnt = 0
            for j in range(n - 1, -1, -1):
                cnt = cnt + 1 if grid[i][j] else 0
                right[i][j] = cnt

        # Up arm length (top to bottom per column)
        up = [[0] * n for _ in range(n)]
        for j in range(n):
            cnt = 0
            for i in range(n):
                cnt = cnt + 1 if grid[i][j] else 0
                up[i][j] = cnt

        # Down arm length (bottom to top per column)
        down = [[0] * n for _ in range(n)]
        for j in range(n):
            cnt = 0
            for i in range(n - 1, -1, -1):
                cnt = cnt + 1 if grid[i][j] else 0
                down[i][j] = cnt

        # The order of a plus sign centered at (i,j) is the minimum of its four arms
        # We track the maximum order over all cells
        best = 0
        for i in range(n):
            for j in range(n):
                order = min(up[i][j], down[i][j], left[i][j], right[i][j])
                if order > best:
                    best = order
        return best