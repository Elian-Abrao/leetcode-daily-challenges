from __future__ import annotations

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # ---------- 1. Find peak index ----------
        # The array first strictly increases, then strictly decreases.
        # We binary search for the peak (maximum element).
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            # Compare mid with its right neighbour to decide direction.
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                # We are on the ascending slope; peak is to the right.
                lo = mid + 1
            else:
                # We are on the descending slope (or at peak); peak is at mid or left.
                hi = mid
        peak = lo  # peak is the index of the maximum element.

        # ---------- 2. Search in the left (increasing) part ----------
        # If found, this is guaranteed to be the minimum index because left part
        # contains smaller indices. We return immediately.
        left_idx = self._binary_search_increasing(mountainArr, target, 0, peak)
        if left_idx != -1:
            return left_idx

        # ---------- 3. Search in the right (decreasing) part ----------
        # If not found on left, search the right side.
        return self._binary_search_decreasing(mountainArr, target, peak + 1, n - 1)

    # ----------------------------------------------------------------
    def _binary_search_increasing(
        self, arr: 'MountainArray', target: int, left: int, right: int
    ) -> int:
        """Standard binary search on a strictly increasing segment."""
        while left <= right:
            mid = (left + right) // 2
            val = arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # ----------------------------------------------------------------
    def _binary_search_decreasing(
        self, arr: 'MountainArray', target: int, left: int, right: int
    ) -> int:
        """Binary search on a strictly decreasing segment."""
        while left <= right:
            mid = (left + right) // 2
            val = arr.get(mid)
            if val == target:
                return mid
            elif val > target:
                # In a decreasing segment, larger values are to the left.
                left = mid + 1
            else:
                right = mid - 1
        return -1