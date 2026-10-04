from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        Finds the minimum number of crossed bricks when drawing a vertical line
        through the wall (excluding the two outer edges).

        Approach:
        - For each row, compute prefix sums (cumulative widths) excluding the
          total width (right edge). These prefix sums represent positions of
          vertical gaps between bricks.
        - Count how many rows have a gap at each position using a hash map.
        - The line that passes through the maximum number of gaps will cross
          the fewest bricks: total_rows - max_gap_count.
        - If no gaps exist (all rows are one brick), the answer is total rows.
        """
        # Edge case: empty wall (not possible per constraints, but safe).
        if not wall:
            return 0

        total_rows = len(wall)
        gap_counter = defaultdict(int)  # position -> count of rows with gap there

        for row in wall:
            cumulative = 0
            # Iterate over all bricks except the last one (the right edge).
            for brick in row[:-1]:
                cumulative += brick
                gap_counter[cumulative] += 1

        # If there are no gaps at all (all rows are a single brick), the
        # max_gap_count is 0, and we must cross all bricks.
        if not gap_counter:
            return total_rows

        # The maximum number of rows that have a gap at the same position.
        max_gaps = max(gap_counter.values())
        # Minimum bricks crossed = total rows - rows with a gap at best position.
        return total_rows - max_gaps