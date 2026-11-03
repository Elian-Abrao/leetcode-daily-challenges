class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        """
        Binary search for the peak in a mountain array.
        The array is strictly increasing then strictly decreasing.
        """
        lo, hi = 0, len(arr) - 1

        # Binary search loop: the peak is the unique index where
        # arr[i] > arr[i+1] for the first time (or equivalently
        # arr[i] > arr[i-1] and arr[i] > arr[i+1]).
        # We compare arr[mid] with arr[mid+1] to decide direction.
        while lo < hi:
            mid = (lo + hi) // 2

            # If we are still on the increasing slope,
            # move the left boundary up.
            if arr[mid] < arr[mid + 1]:
                # Peak is to the right of mid.
                lo = mid + 1
            else:
                # arr[mid] > arr[mid+1], so we are on the decreasing slope
                # or exactly at the peak. Narrow from the right.
                hi = mid

        # lo == hi, which is the peak index.
        return lo