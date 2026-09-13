from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Returns the length of the longest harmonious subsequence.
        A harmonious subsequence has max - min == 1, so it can only
        contain two distinct values that differ by exactly 1.
        The optimal subsequence consists of all occurrences of those
        two values. Thus we just need to find the pair of adjacent
        numbers (x, x+1) with the maximum total frequency.
        """
        # Step 1: count frequencies of each number
        freq = Counter(nums)

        max_len = 0

        # Step 2: for each number x, check if x+1 exists
        for x in freq:
            if x + 1 in freq:
                # total length = count(x) + count(x+1)
                current = freq[x] + freq[x + 1]
                if current > max_len:
                    max_len = current

        return max_len