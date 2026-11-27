class Solution:
    def possibleToStamp(self, grid: list[list[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])

        # If the stamp does not fit in either dimension, we cannot place any stamp.
        # Then it is only possible when there is no empty cell to cover.
        if stampHeight > m or stampWidth > n:
            # Check if any empty cell exists
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0:
                        return False
            return True

        # ---------- 2‑D prefix sum of occupied cells (1‑based) ----------
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pref[i + 1][j + 1] = (grid[i][j] +
                                      pref[i][j + 1] +
                                      pref[i + 1][j] -
                                      pref[i][j])

        # ---------- Difference array for coverage counting ----------
        # diff[i][j] will be turned into the number of stamps covering cell (i,j)
        diff = [[0] * (n + 1) for _ in range(m + 1)]

        # Enumerate every possible top‑left corner of a stamp placement.
        for i in range(m - stampHeight + 1):
            r2 = i + stampHeight - 1          # bottom row of the stamp
            for j in range(n - stampWidth + 1):
                c2 = j + stampWidth - 1       # rightmost column of the stamp
                # Number of occupied cells inside this rectangle.
                ones = (pref[r2 + 1][c2 + 1] - pref[i][c2 + 1] -
                        pref[r2 + 1][j] + pref[i][j])
                if ones == 0:                 # entirely free -> valid placement
                    # Mark the rectangle in the difference array.
                    diff[i][j] += 1
                    diff[i][j + stampWidth] -= 1
                    diff[i + stampHeight][j] -= 1
                    diff[i + stampHeight][j + stampWidth] += 1

        # ---------- Build coverage counts from the difference array ----------
        # Horizontal prefix sum (row‑wise)
        for i in range(m + 1):
            row = diff[i]
            for j in range(1, n + 1):
                row[j] += row[j - 1]

        # Vertical prefix sum (column‑wise)
        for j in range(n + 1):
            for i in range(1, m + 1):
                diff[i][j] += diff[i - 1][j]

        # ---------- Final check: every empty cell must be covered ----------
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and diff[i][j] == 0:
                    return False
        return True