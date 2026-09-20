from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search for the leftmost index of the best window of size k.
        # The array is sorted, so the closest k elements must form a contiguous subarray.
        n = len(arr)
        left, right = 0, n - k  # window of size k can start from 0 to n-k

        while left < right:
            mid = (left + right) // 2
            # Compare the two candidates at the edges of the current window:
            # arr[mid] (left edge) and arr[mid+k] (right edge of the next possible window)
            # If the right edge is closer to x, the window should shift right.
            # Tie-breaking: if distances equal, prefer the smaller value (arr[mid]),
            # so we keep left in that case.
            if abs(arr[mid] - x) > abs(arr[mid + k] - x):
                left = mid + 1
            else:
                right = mid

        # left is now the start index of the optimal window
        return arr[left:left + k]