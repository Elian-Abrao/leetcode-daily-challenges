import math
from typing import List

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        # At least one dart can always be covered.
        ans = 1

        # Convert to list of tuples for faster access.
        points = [(x, y) for x, y in darts]

        # Consider every pair of points as potential boundary points.
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                d_sq = dx * dx + dy * dy

                # Distance between the two points must be <= 2r.
                if d_sq > 4 * r * r:
                    continue

                # Midpoint between the two points.
                mx = (x1 + x2) / 2.0
                my = (y1 + y2) / 2.0
                d = math.sqrt(d_sq)
                half_d = d / 2.0

                # Perpendicular distance from midpoint to circle centers.
                h_sq = r * r - half_d * half_d
                h = math.sqrt(max(0.0, h_sq))

                # Unit perpendicular vector scaled by h/d.
                factor = h / d   # d > 0 because points are distinct.

                # Two possible centers (symmetric about the line p1-p2).
                for sign in (1, -1):
                    cx = mx + sign * (-dy) * factor
                    cy = my + sign * dx * factor

                    # Count how many points lie inside or exactly on this circle.
                    cnt = 0
                    for px, py in points:
                        # Use squared distance to avoid another sqrt.
                        if (px - cx) * (px - cx) + (py - cy) * (py - cy) <= r * r + 1e-9:
                            cnt += 1
                    ans = max(ans, cnt)

        return ans