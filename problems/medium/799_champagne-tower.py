class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # We'll simulate the champagne flow row by row
        # Current row stores the amount of champagne poured into each glass (can exceed 1)
        current_row = [poured]
        
        # Simulate for each row from 0 to query_row
        for row in range(query_row):
            # Next row will have row + 2 glasses (0-indexed: row 0 has 1 glass, row 1 has 2, etc.)
            next_row = [0.0] * (row + 2)
            
            # Process each glass in current row
            for col in range(len(current_row)):
                # Amount of champagne in this glass
                amount = current_row[col]
                
                # If this glass has more than 1 cup, overflow happens
                if amount > 1.0:
                    overflow = amount - 1.0
                    # Split overflow equally to two glasses below
                    # Glass at (row, col) overflows to (row+1, col) and (row+1, col+1)
                    next_row[col] += overflow / 2.0
                    next_row[col + 1] += overflow / 2.0
            
            # Move to next row
            current_row = next_row
        
        # After simulation, current_row represents the query_row
        # Return the amount in query_glass, capped at 1.0 (glass can't hold more than 1 cup)
        return min(1.0, current_row[query_glass])