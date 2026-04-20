from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Handle empty input defensively (though constraints guarantee non-empty)
        if not nums:
            return 0

        # The minimal possible largest sum is at least the maximum element
        left, right = max(nums), sum(nums)

        # Greedy feasibility check:
        # Given a candidate maximum subarray sum 'limit',
        # determine if we can split nums into <= k subarrays such that
        # no subarray has sum > limit.
        def can(limit: int) -> bool:
            subarrays = 1
            current_sum = 0
            for val in nums:
                # If adding current value keeps within limit, extend current subarray
                if current_sum + val <= limit:
                    current_sum += val
                else:
                    # Start a new subarray with this value
                    subarrays += 1
                    current_sum = val
                    # Early exit if we already need more than k subarrays
                    if subarrays > k:
                        return False
            return True

        # Binary search on the answer between left and right (inclusive).
        # Invariant: 'left' is feasible, 'right' is infeasible initially.
        while left < right:
            mid = (left + right) // 2
            if can(mid):
                # If feasible, try a smaller maximum sum
                right = mid
            else:
                # If not feasible, need a larger maximum sum
                left = mid + 1

        # Left is the minimal feasible maximum subarray sum
        return left