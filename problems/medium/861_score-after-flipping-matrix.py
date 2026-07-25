from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Strategy:
        # 1. Always flip rows to ensure the leftmost bit (MSB) is 1
        #    because MSB contributes the most to the binary value.
        # 2. After fixing all rows to have MSB = 1, decide for each column
        #    whether to flip it by maximizing the count of 1s in that column.
        
        # Step 1: Flip rows if first element is 0
        # We don't actually modify the grid; we track the flip state
        # and calculate effective values dynamically.
        
        # After flipping rows to ensure first column is all 1s,
        # the leftmost column contributes: m * 2^(n-1)
        score = m * (1 << (n - 1))
        
        # Step 2: For each remaining column (from 1 to n-1),
        # count how many 1s we would have after row flips.
        # Then decide whether to flip the column to maximize 1s count.
        for col in range(1, n):
            # Count how many 1s are in this column after row flips
            # Row i is flipped if grid[i][0] == 0
            count_ones = 0
            for row in range(m):
                # Determine the effective value at grid[row][col]
                # after potentially flipping row
                if grid[row][0] == 0:
                    # Row is flipped, so toggle the bit
                    effective_val = 1 - grid[row][col]
                else:
                    # Row is not flipped
                    effective_val = grid[row][col]
                
                count_ones += effective_val
            
            # We want to maximize the number of 1s in this column.
            # If count_ones < m - count_ones, flip the column to get more 1s.
            max_ones = max(count_ones, m - count_ones)
            
            # Contribution of this column to the score
            score += max_ones * (1 << (n - 1 - col))
        
        return score