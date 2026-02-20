from __future__ import annotations
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0  # Safety for empty input (not in constraints, but robust)

        # Left-to-right pass: ensure each child has more candies than left neighbor if rating is higher
        left = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # Right-to-left pass: ensure each child has more candies than right neighbor if rating is higher
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        # Combine both passes: for each child, take the maximum required candies
        total = 0
        for i in range(n):
            total += left[i] if left[i] >= right[i] else right[i]

        return total