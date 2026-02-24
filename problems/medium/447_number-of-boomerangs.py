from __future__ import annotations

from typing import List
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        """
        Count boomerangs in O(n^2) time by fixing center i and counting
        distances to all other points j. For a fixed i, if there are
        cnt points at the same distance from i, they contribute cnt*(cnt-1)
        boomerangs (ordered pairs (j, k)).
        """
        n = len(points)
        if n <= 1:
            return 0

        total = 0
        for i in range(n):
            xi, yi = points[i]
            dist_count = defaultdict(int)

            # Count how many points are at each squared distance from i
            for j in range(n):
                if i == j:
                    continue
                dx = points[j][0] - xi
                dy = points[j][1] - yi
                dist_sq = dx * dx + dy * dy
                dist_count[dist_sq] += 1

            # For each distance with frequency f, there are f*(f-1) boomerangs
            for freq in dist_count.values():
                if freq > 1:
                    total += freq * (freq - 1)

        return total