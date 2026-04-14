from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Greedy O(n) solution:
        - Maintain the furthest index we can reach from all positions up to the current processing point.
        - Maintain the end boundary of the current jump range. When we reach this boundary,
          we must perform another jump, increasing the answer and extending the boundary
          to the previously computed furthest.
        - This approach guarantees the minimum number of jumps because we always expand within
          the current window as far as possible before committing to the next jump.
        """
        n = len(nums)
        if n <= 1:
            return 0  # Already at the last index; no jumps needed.

        jumps = 0           # Number of jumps used to reach the last index.
        current_end = 0     # The furthest index reachable with the current number of jumps.
        furthest = 0          # The furthest index reachable with one more jump from positions <= i.

        for i in range(n - 1):  # We don't need to jump from the last index.
            # Update the furthest reachable index considering position i.
            furthest = max(furthest, i + nums[i])

            # If we've reached the end of the current jump's coverage, it's time to jump.
            if i == current_end:
                jumps += 1
                current_end = furthest

                # Optional early exit: if the new boundary already covers the last index.
                if current_end >= n - 1:
                    break

        return jumps