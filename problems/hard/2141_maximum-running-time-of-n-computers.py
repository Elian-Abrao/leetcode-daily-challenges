from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """
        Binary search the maximum running time T.
        Feasibility condition: total usable capacity >= n * T,
        where usable capacity from a battery is min(b, T).
        """
        total = sum(batteries)
        # Upper bound: we cannot exceed total energy divided equally.
        left, right = 1, total // n

        while left <= right:
            mid = (left + right) // 2
            # Compute sum(min(b, mid))
            usable = 0
            for b in batteries:
                if b < mid:
                    usable += b
                else:
                    usable += mid
                # Early exit if already enough
                if usable >= n * mid:
                    break
            if usable >= n * mid:
                left = mid + 1
            else:
                right = mid - 1

        return right