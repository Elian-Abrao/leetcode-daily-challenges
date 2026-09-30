from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        Counts unique k-diff pairs (a, b) where |a - b| == k.
        Uses frequency map and handles k == 0 separately.
        """
        # freq[v] = number of occurrences of v
        freq = Counter(nums)

        # For k == 0, a pair exists for each value that appears at least twice
        if k == 0:
            # Count values that have duplicates
            return sum(1 for v in freq if freq[v] >= 2)

        # For k > 0, check each unique value and see if value + k exists.
        # We only check in one direction (value + k) to avoid double counting.
        pairs = 0
        for v in freq:
            if v + k in freq:
                pairs += 1

        return pairs