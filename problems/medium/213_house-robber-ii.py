from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # With one house, the circle constraint disappears.
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: List[int]) -> int:
            # prev_two = best up to house i-2
            # prev_one = best up to house i-1
            prev_two = 0
            prev_one = 0

            for amount in houses:
                # Either skip current house, or take it and add the best non-adjacent result.
                current = max(prev_one, prev_two + amount)
                prev_two = prev_one
                prev_one = current

            return prev_one

        # In a circle, we cannot take both first and last houses.
        # So solve two linear cases and keep the better one:
        # 1) exclude the first house
        # 2) exclude the last house
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))