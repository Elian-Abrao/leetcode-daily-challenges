from __future__ import annotations

class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        """
        Returns the minimum size of a set S such that every interval
        contains at least two elements from S.
        """
        # Sort intervals by their end value ascending.
        intervals.sort(key=lambda x: x[1])

        # p1 is the largest chosen point, p2 is the second largest.
        p1 = p2 = -1
        ans = 0

        for s, e in intervals:
            # Count how many of the two chosen points are inside the interval.
            covered = 0
            if s <= p1 <= e:
                covered += 1
            if s <= p2 <= e:
                covered += 1

            if covered >= 2:
                continue
            elif covered == 1:
                # Need exactly one more point.
                ans += 1
                if e > p1:
                    # Add the rightmost point, which is larger than p1.
                    p2 = p1
                    p1 = e
                else:  # e == p1 (cannot be less because sorted by end)
                    # Adding e would duplicate; use e-1 instead.
                    # e-1 >= s and e-1 > p2 (since s > p2 by the elif condition).
                    p2 = e - 1
                    # p1 remains unchanged (still the largest).
            else:  # covered == 0
                # Need two new points: e-1 and e.
                ans += 2
                p2 = e - 1
                p1 = e

        return ans