from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # With k == 0, distinct indices can never be at distance 0.
        if k == 0:
            return False

        last_index = {}

        for index, value in enumerate(nums):
            # Only the most recent occurrence matters, because it gives
            # the smallest possible distance to the current index.
            if value in last_index and index - last_index[value] <= k:
                return True

            # Update after checking so we compare against a previous index.
            last_index[value] = index

        # No valid pair was found.
        return False