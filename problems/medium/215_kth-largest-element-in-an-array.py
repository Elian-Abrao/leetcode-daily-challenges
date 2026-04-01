from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Constraints give a very small value range, so counting is faster
        # and simpler than full sorting or randomized quickselect.
        offset = 10000
        counts = [0] * 20001

        # Count every value once; duplicates matter for the k-th largest order.
        for value in nums:
            counts[value + offset] += 1

        remaining = k

        # Walk from the largest possible value downwards.
        # As soon as we have skipped k elements, we found the answer.
        for index in range(20000, -1, -1):
            freq = counts[index]
            if freq == 0:
                continue

            remaining -= freq
            if remaining <= 0:
                return index - offset

        # Constraints guarantee a valid answer, so execution should never reach here.
        return 0