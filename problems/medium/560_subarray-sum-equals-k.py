from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Maps each prefix sum to its frequency seen so far.
        # Initial {0: 1} handles subarrays that start from the beginning.
        prefix_sums = {0: 1}
        running_sum = 0
        total = 0

        for num in nums:
            running_sum += num

            # A previous prefix sum of running_sum - k means the segment
            # between them sums to exactly k.
            total += prefix_sums.get(running_sum - k, 0)

            # Store the current prefix sum for future subarrays.
            prefix_sums[running_sum] = prefix_sums.get(running_sum, 0) + 1

        return total