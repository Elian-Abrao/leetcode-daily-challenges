from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Incrementing n - 1 elements by 1 is equivalent to decrementing
        # the one excluded element by 1. So the optimal target is the
        # current minimum value, minimizing total required decrements.
        minimum_value = min(nums)

        moves = 0
        for value in nums:
            # Each element must effectively be reduced to the minimum.
            # Python integers safely handle the full constraint range.
            moves += value - minimum_value

        return moves