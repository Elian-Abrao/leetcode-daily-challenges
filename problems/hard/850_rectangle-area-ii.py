class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        MOD = 1_000_000_007
        
        # Collect all distinct boundary coordinates.
        xs = set()
        ys = set()
        for x1, y1, x2, y2 in rectangles:
            xs.add(x1)
            xs.add(x2)
            ys.add(y1)
            ys.add(y2)
        
        xs = sorted(xs)
        ys = sorted(ys)
        
        # Map coordinate -> index in the sorted list.
        x_idx = {x: i for i, x in enumerate(xs)}
        y_idx = {y: i for i, y in enumerate(ys)}
        
        m = len(xs) - 1          # number of x‑intervals (cells in x direction)
        n = len(ys) - 1          # number of y‑intervals (cells in y direction)
        
        # covered[i][j] will be True if the cell (i,j) is covered by any rectangle.
        covered = [bytearray(n) for _ in range(m)]
        
        # Pre‑compute byte patterns of ones for every possible segment length.
        ones = [b'\x01' * length for length in range(n + 1)]
        
        # Mark every rectangle on the grid.
        for x1, y1, x2, y2 in rectangles:
            ix1 = x_idx[x1]
            ix2 = x_idx[x2]          # exclusive in cell indexing
            iy1 = y_idx[y1]
            iy2 = y_idx[y2]          # exclusive in cell indexing
            
            seg_len = iy2 - iy1
            pattern = ones[seg_len]   # bytes of length seg_len filled with 1
            
            # For every x‑interval inside the rectangle, fill the whole y‑segment.
            for i in range(ix1, ix2):
                covered[i][iy1:iy2] = pattern
        
        # Sum the areas of all covered cells.
        total = 0
        for i in range(m):
            row = covered[i]
            dx = xs[i + 1] - xs[i]
            for j in range(n):
                if row[j]:
                    dy = ys[j + 1] - ys[j]
                    total = (total + dx * dy) % MOD
        
        return total