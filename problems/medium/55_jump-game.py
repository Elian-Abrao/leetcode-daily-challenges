from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # If the array has a single element, we're already at the last index.
        if len(nums) == 1:
            return True

        max_reach = 0  # Furthest index we can reach using elements up to current position.

        for i, jump in enumerate(nums):
            # If current index is beyond what we can reach, we are stuck.
            if i > max_reach:
                return False

            # Update the furthest reach from this position.
            max_reach = max(max_reach, i + jump)

            # Early exit: if we can reach or pass the last index, success.
            if max_reach >= len(nums) - 1:
                return True

        # After processing all positions, check if last index is reachable.
        return max_reach >= len(nums) - 1