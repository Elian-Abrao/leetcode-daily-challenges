class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only 1 row or string shorter than numRows, no zigzag needed
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list to hold characters for each row
        rows = [[] for _ in range(numRows)]
        
        # Track current row and direction of movement
        current_row = 0
        going_down = False
        
        # Traverse each character and assign to appropriate row
        for char in s:
            rows[current_row].append(char)
            
            # Change direction at the top or bottom row
            # At row 0, we must go down; at row numRows-1, we must go up
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to next row based on direction
            current_row += 1 if going_down else -1
        
        # Concatenate all rows to form the final result
        return ''.join(''.join(row) for row in rows)