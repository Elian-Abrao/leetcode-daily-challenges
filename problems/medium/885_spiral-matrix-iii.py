class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        """
        Simulate the clockwise spiral walk, generating positions in order.
        The spiral expands by increasing step length after every two direction changes.
        We record only positions that lie within the grid boundaries.
        """
        # Direction vectors: east, south, west, north (clockwise order)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        result = []
        r, c = rStart, cStart
        
        # Step length for current direction segment; increases every 2 turns
        step = 1
        direction_index = 0
        
        # We need to collect exactly rows * cols positions
        total_cells = rows * cols
        
        while len(result) < total_cells:
            # For the current direction, walk 'step' cells
            for _ in range(step):
                # Check if current position is inside the grid
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
                    # Early exit if we've collected everything
                    if len(result) == total_cells:
                        return result
                # Move to the next cell in the current direction
                dr, dc = directions[direction_index]
                r += dr
                c += dc
            
            # Change direction clockwise
            direction_index = (direction_index + 1) % 4
            
            # After every two direction changes, increase the step length
            # This creates the expanding spiral pattern
            if direction_index % 2 == 0:
                step += 1
        
        return result