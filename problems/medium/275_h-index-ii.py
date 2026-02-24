from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Binary search over possible h values in [0, n].
        For a candidate h, check if there are at least h papers with >= h citations.
        Since the array is sorted ascending, the h-th largest paper corresponds to index n - h.
        """
        n = len(citations)
        lo, hi = 0, n
        best = 0  # stores the maximum feasible h found so far

        while lo <= hi:
            mid = (lo + hi) // 2  # candidate h

            # Feasibility check:
            # - If mid == 0, trivially feasible (0 papers required).
            # - Otherwise, need citations[n - mid] >= mid, meaning there are at least mid papers
            #   with at least mid citations.
            if mid == 0:
                feasible = True
            else:
                feasible = citations[n - mid] >= mid

            if feasible:
                best = mid      # update best possible h
                lo = mid + 1      # try to see if a larger h is possible
            else:
                hi = mid - 1      # reduce h and try again

        return best