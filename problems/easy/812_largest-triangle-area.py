from __future__ import annotations

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        """
        Returns the maximum area of any triangle formed by three distinct points.
        Uses the shoelace formula and brute-force triple loop over all combinations.
        Time: O(n^3) where n = len(points) (max 50 → ~125k iterations).
        Space: O(1).
        """
        n = len(points)
        max_area = 0.0

        # Iterate over all unordered triples (i < j < k)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]

                    # Shoelace formula: area = 0.5 * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
                    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0

                    if area > max_area:
                        max_area = area

        return max_area