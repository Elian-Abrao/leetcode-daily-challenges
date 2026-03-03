from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Handle empty input defensively; according to constraints this is unlikely
        if not nums:
            return 0

        # tails[i] will be the smallest possible tail value of an increasing subsequence
        # of length i+1. This allows us to maintain the best potential subsequences efficiently.
        tails: List[int] = []

        for value in nums:
            # Locate the insertion point for value in tails to maintain increasing order.
            # This is effectively performing a binary search in O(log n).
            idx = bisect.bisect_left(tails, value)

            if idx == len(tails):
                # value extends largest subsequence found so far
                tails.append(value)
            else:
                # Replace existing tail with a smaller value to potentially enable longer LIS later
                tails[idx] = value

        # The length of tails equals the length of the LIS
        return len(tails)