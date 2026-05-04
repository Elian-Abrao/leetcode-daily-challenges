from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to track seen digits in rows, columns, and 3x3 boxes
        # Each set stores tuples of (digit, index) to identify violations
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Single pass through the board - O(81) = O(1) since board is fixed 9x9
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                
                # Skip empty cells - only validate filled digits
                if cell == '.':
                    continue
                
                # Check if digit already exists in current row
                if cell in rows[i]:
                    return False
                rows[i].add(cell)
                
                # Check if digit already exists in current column
                if cell in cols[j]:
                    return False
                cols[j].add(cell)
                
                # Calculate which 3x3 box this cell belongs to
                # Box index: 0-8, mapping (row, col) to box number
                # Formula: (row // 3) * 3 + (col // 3)
                box_idx = (i // 3) * 3 + (j // 3)
                
                # Check if digit already exists in current 3x3 box
                if cell in boxes[box_idx]:
                    return False
                boxes[box_idx].add(cell)
        
        # All constraints satisfied - valid sudoku configuration
        return True