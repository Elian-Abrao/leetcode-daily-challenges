from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Handle empty input defensively
        if not envelopes:
            return 0

        # Strategy:
        # 1) Sort envelopes by width asc. For envelopes with the same width, sort by height desc.
        #    This ensures that envelopes with equal width won't be counted in the LIS on heights.
        # 2) Compute the LIS (strictly increasing) on the sequence of heights.
        #    The length of this LIS is the maximum number of envelopes that fit.
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Extract heights and perform patience sorting style LIS in O(n log n)
        heights = [h for _, h in envelopes]
        dp: List[int] = []  # dp[k] = smallest possible tail value of an increasing subsequence of length k+1

        for h in heights:
            # Find the insertion point for h in dp to maintain strictly increasing subsequences
            idx = bisect.bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h

        return len(dp)