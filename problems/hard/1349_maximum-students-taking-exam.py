from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        
        # Convert each row to a bitmask representing valid seats
        # Bit i is 1 if seat i is available ('.')
        valid_masks = []
        for row in seats:
            mask = 0
            for j in range(n):
                if row[j] == '.':
                    mask |= (1 << j)
            valid_masks.append(mask)
        
        # Check if a seating arrangement (mask) is valid for a row
        # No two adjacent students in the same row
        def is_valid_arrangement(mask):
            # Check no two adjacent bits are set
            return (mask & (mask << 1)) == 0
        
        # Check if current row arrangement is compatible with previous row
        # Students can't see upper-left or upper-right neighbors
        def is_compatible(curr_mask, prev_mask):
            # Check upper-left: if bit i is set in curr, bit i-1 shouldn't be set in prev
            if (curr_mask & (prev_mask << 1)) != 0:
                return False
            # Check upper-right: if bit i is set in curr, bit i+1 shouldn't be set in prev
            if (curr_mask & (prev_mask >> 1)) != 0:
                return False
            return True
        
        # Precompute all valid arrangements for each row
        valid_arrangements = []
        for row_idx in range(m):
            arrangements = []
            valid_mask = valid_masks[row_idx]
            # Try all possible subsets of valid seats
            mask = valid_mask
            while True:
                # Check if this arrangement has no adjacent students
                if is_valid_arrangement(mask):
                    arrangements.append(mask)
                # Move to next subset (iterate through all subsets of valid_mask)
                if mask == 0:
                    break
                mask = (mask - 1) & valid_mask
            valid_arrangements.append(arrangements)
        
        # DP: dp[row][mask] = max students we can place in rows 0..row
        # where 'mask' is the seating arrangement in 'row'
        dp = [{}for _ in range(m)]
        
        # Initialize first row
        for mask in valid_arrangements[0]:
            dp[0][mask] = bin(mask).count('1')
        
        # Fill DP table row by row
        for row in range(1, m):
            for curr_mask in valid_arrangements[row]:
                max_students = 0
                # Try all valid arrangements from previous row
                for prev_mask in dp[row - 1]:
                    if is_compatible(curr_mask, prev_mask):
                        max_students = max(max_students, dp[row - 1][prev_mask])
                
                # Add students in current row
                dp[row][curr_mask] = max_students + bin(curr_mask).count('1')
        
        # Return maximum students across all arrangements in last row
        return max(dp[m - 1].values()) if dp[m - 1] else 0