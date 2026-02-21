from __future__ import annotations
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Result container
        res: List[List[int]] = []
        i = 0
        n = len(intervals)
        # Work with a local copy of newInterval to allow in-place growth during merge
        ni, ne = newInterval

        # 1) Add all intervals that end before the new interval starts (no overlap)
        while i < n and intervals[i][1] < ni:
            res.append(intervals[i])
            i += 1

        # 2) Merge all intervals that overlap with the new interval
        while i < n and intervals[i][0] <= ne:
            # Expand the new merged interval to include the overlapping interval
            ni = min(ni, intervals[i][0])
            ne = max(ne, intervals[i][1])
            i += 1

        # 3) Append the merged new interval
        res.append([ni, ne])

        # 4) Append any remaining intervals after the merge
        while i < n:
            res.append(intervals[i])
            i += 1

        return res