from typing import List
from collections import Counter

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        Determine if four points form a valid square.
        Uses squared distances to avoid floating-point errors.
        A square must have exactly 4 equal side lengths and 2 equal diagonal lengths,
        with side > 0 and diagonal^2 = 2 * side^2.
        """
        # Squared Euclidean distance between two points
        def squared_dist(a: List[int], b: List[int]) -> int:
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            return dx * dx + dy * dy

        # Compute all 6 pairwise squared distances
        points = [p1, p2, p3, p4]
        distances = []
        for i in range(4):
            for j in range(i + 1, 4):
                distances.append(squared_dist(points[i], points[j]))

        # Count frequency of each distance
        freq = Counter(distances)

        # A valid square must have exactly 2 distinct distances:
        # 4 sides and 2 diagonals
        if len(freq) != 2:
            return False

        # Retrieve the two distinct distances
        d1, d2 = freq.keys()
        cnt1, cnt2 = freq[d1], freq[d2]

        # There should be one distance appearing 4 times (sides) and another appearing 2 times (diagonals)
        if not ((cnt1 == 4 and cnt2 == 2) or (cnt1 == 2 and cnt2 == 4)):
            return False

        # Side length must be positive, and diagonal^2 must equal 2 * side^2
        side_sq = min(d1, d2)   # sides are the shorter distance
        diag_sq = max(d1, d2)   # diagonals are the longer distance
        if side_sq == 0:        # zero-length side means degenerate (all points same)
            return False
        return diag_sq == 2 * side_sq