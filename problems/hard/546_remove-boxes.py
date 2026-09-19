from functools import lru_cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @lru_cache(maxsize=None)
        def dp(l: int, r: int, k: int) -> int:
            """
            Maximum points obtainable from boxes[l..r] (inclusive),
            with k extra boxes of the same color as boxes[l] already
            placed to the left (not yet removed).
            """
            if l > r:
                return 0

            # Option 1: remove boxes[l] together with the k extra boxes immediately.
            # Points = (k+1)^2, then solve for the rest (l+1..r) with no extra.
            best = (k + 1) * (k + 1) + dp(l + 1, r, 0)

            # Option 2: keep boxes[l] to merge later with another same‑colored box.
            # Look for a position i > l where boxes[i] == boxes[l].
            for i in range(l + 1, r + 1):
                if boxes[i] == boxes[l]:
                    # Remove the inner segment (l+1..i-1) independently.
                    # Then boxes[l] and boxes[i] become adjacent,
                    # increasing the 'extra' count by 1 (the original k + the kept box[l]).
                    best = max(best, dp(l + 1, i - 1, 0) + dp(i, r, k + 1))

            return best

        return dp(0, n - 1, 0)