from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Build the row in place to keep extra space linear, as requested.
        row = [1] * (rowIndex + 1)

        # Rows 0 and 1 are already correct with the initialization above.
        for current_row in range(2, rowIndex + 1):
            # Update from right to left so values from the previous row
            # are still available when computing the new row.
            for j in range(current_row - 1, 0, -1):
                row[j] += row[j - 1]

        # The list now represents the exact 0-indexed row requested.
        return row