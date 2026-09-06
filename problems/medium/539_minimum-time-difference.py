from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert all "HH:MM" strings to total minutes (0 - 1439)
        minutes = []
        for tp in timePoints:
            h, m = map(int, tp.split(':'))
            minutes.append(h * 60 + m)

        # Sort the minute values to enable linear scanning
        minutes.sort()

        # If any duplicate exists, the difference is 0 (earliest possible)
        # This check is optional but saves scanning in large lists with duplicates.
        for i in range(1, len(minutes)):
            if minutes[i] == minutes[i-1]:
                return 0

        # Minimum difference initially set to a large value (full day)
        min_diff = 1440  # 24*60

        # Compare adjacent times in sorted order
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i-1]
            if diff < min_diff:
                min_diff = diff

        # Handle circular wrap-around: difference between last and first + 24h
        wrap_diff = 1440 - minutes[-1] + minutes[0]
        if wrap_diff < min_diff:
            min_diff = wrap_diff

        return min_diff