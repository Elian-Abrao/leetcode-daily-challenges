from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Track the best total up to the previous house and the house before that.
        # This is enough because the transition only depends on i - 1 and i - 2.
        prev_two = 0
        prev_one = 0

        for amount in nums:
            # Either skip this house and keep the previous best,
            # or rob it and add its money to the best non-adjacent total.
            current = max(prev_one, prev_two + amount)

            # Shift the DP window forward for the next iteration.
            prev_two = prev_one
            prev_one = current

        # Works for all valid inputs, including a single house or all zeros.
        return prev_one