from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # Count total number of 1s
        ones = sum(arr)
        
        # If no 1s, all parts are zero - any valid split works
        if ones == 0:
            return [0, len(arr) - 1]
        
        # If ones count is not divisible by 3, impossible to split equally
        if ones % 3 != 0:
            return [-1, -1]
        
        # Each part must have exactly ones_per_part ones
        ones_per_part = ones // 3
        
        # Find the start positions of the first 1 in each of the three parts
        # Strategy: locate where each part's significant bits begin
        first_one_positions = []
        count = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1
                # Mark start of each third
                if count == 1 or count == ones_per_part + 1 or count == 2 * ones_per_part + 1:
                    first_one_positions.append(i)
        
        # Now we have three starting positions for the three parts
        start1, start2, start3 = first_one_positions
        
        # Check if all three parts match bit by bit
        # We need to verify that the binary representations are identical
        # Continue until we reach the end of the array (third part defines the length)
        while start3 < len(arr):
            # All three positions must have the same bit value
            if arr[start1] != arr[start2] or arr[start2] != arr[start3]:
                return [-1, -1]
            start1 += 1
            start2 += 1
            start3 += 1
        
        # If we've successfully matched all bits:
        # - First part ends at start1 - 1 (since start1 has moved past the matching region)
        # - Second part starts at start1 and ends at start2 - 1
        # - Third part starts at start2
        # Return [i, j] where:
        #   - First part: arr[0..i]
        #   - Second part: arr[i+1..j-1]
        #   - Third part: arr[j..end]
        # So i = start1 - 1, j = start2
        return [start1 - 1, start2]