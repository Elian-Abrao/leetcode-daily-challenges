from typing import List

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Use sets and counters to track lamp positions and illuminated lines
        # A lamp illuminates its row, column, and both diagonals
        
        # Track actual lamp positions (deduplicated)
        lamp_positions = set()
        
        # Count how many lamps illuminate each row, column, and diagonal
        row_count = {}
        col_count = {}
        diag1_count = {}  # main diagonal: row - col is constant
        diag2_count = {}  # anti-diagonal: row + col is constant
        
        # Add all lamps (handle duplicates via set)
        for r, c in lamps:
            pos = (r, c)
            if pos in lamp_positions:
                continue  # Skip duplicates
            
            lamp_positions.add(pos)
            row_count[r] = row_count.get(r, 0) + 1
            col_count[c] = col_count.get(c, 0) + 1
            diag1_count[r - c] = diag1_count.get(r - c, 0) + 1
            diag2_count[r + c] = diag2_count.get(r + c, 0) + 1
        
        result = []
        
        # Process each query
        for qr, qc in queries:
            # Check if the queried cell is illuminated
            # A cell is illuminated if any lamp is on the same row, col, or diagonal
            is_illuminated = (
                row_count.get(qr, 0) > 0 or
                col_count.get(qc, 0) > 0 or
                diag1_count.get(qr - qc, 0) > 0 or
                diag2_count.get(qr + qc, 0) > 0
            )
            
            result.append(1 if is_illuminated else 0)
            
            # Turn off the lamp at (qr, qc) and all 8 adjacent lamps
            # Directions: center + 8 neighbors
            directions = [
                (0, 0),   # center
                (-1, -1), (-1, 0), (-1, 1),  # top row
                (0, -1),           (0, 1),   # middle row
                (1, -1),  (1, 0),  (1, 1)    # bottom row
            ]
            
            for dr, dc in directions:
                nr, nc = qr + dr, qc + dc
                
                # Check bounds (though n can be huge, lamps are within bounds by problem)
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                
                pos = (nr, nc)
                if pos in lamp_positions:
                    # Turn off this lamp
                    lamp_positions.remove(pos)
                    
                    # Decrease counts for this lamp's illuminated lines
                    row_count[nr] -= 1
                    if row_count[nr] == 0:
                        del row_count[nr]
                    
                    col_count[nc] -= 1
                    if col_count[nc] == 0:
                        del col_count[nc]
                    
                    d1 = nr - nc
                    diag1_count[d1] -= 1
                    if diag1_count[d1] == 0:
                        del diag1_count[d1]
                    
                    d2 = nr + nc
                    diag2_count[d2] -= 1
                    if diag2_count[d2] == 0:
                        del diag2_count[d2]
        
        return result