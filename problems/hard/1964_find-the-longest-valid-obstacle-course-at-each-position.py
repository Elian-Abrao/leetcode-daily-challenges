from typing import List
from bisect import bisect_right

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # tails[i] = smallest possible last height of a non-decreasing subsequence of length i+1
        tails = []
        ans = []

        for h in obstacles:
            # Find the first element in tails that is strictly greater than h.
            # Using bisect_right allows equal heights to extend the subsequence,
            # which matches the non-decreasing requirement.
            pos = bisect_right(tails, h)

            if pos == len(tails):
                # Append: current height can form a longer subsequence
                tails.append(h)
            else:
                # Replace: a smaller (or equal) last element at this length
                tails[pos] = h

            # Length of the longest valid course ending at this obstacle
            ans.append(pos + 1)

        return ans