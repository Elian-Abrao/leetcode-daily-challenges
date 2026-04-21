from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Return an empty list for non-positive input defensively
        if numRows <= 0:
            return []
        
        # The first row of Pascal's triangle
        triangle: List[List[int]] = [[1]]
        
        # Build subsequent rows iteratively
        for row_num in range(1, numRows):
            prev_row = triangle[-1]
            # Each new row starts with 1
            new_row: List[int] = [1]
            # Fill the interior values as the sum of two above numbers
            for i in range(1, row_num):
                new_row.append(prev_row[i - 1] + prev_row[i])
            # End with 1
            new_row.append(1)
            triangle.append(new_row)
        
        return triangle