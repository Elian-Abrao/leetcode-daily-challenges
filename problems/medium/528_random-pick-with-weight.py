from typing import List
import random
import bisect

class Solution:
    def __init__(self, w: List[int]) -> None:
        """
        Precompute prefix sums of weights.
        prefix[i] = sum of weights[0..i] (inclusive).
        total = sum of all weights.
        """
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        """
        Randomly pick an index with probability proportional to weight.
        Use a random integer in [1, total] and binary search on prefix sums.
        """
        # Random target in [1, self.total] (inclusive)
        target = random.randint(1, self.total)

        # bisect_left returns the first index with prefix[i] >= target
        # Because prefix is non‑decreasing, binary search is O(log n)
        return bisect.bisect_left(self.prefix, target)