from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # Fewer than 3 bars cannot form a container.
        if n < 3:
            return 0

        left = 0
        right = n - 1

        # These track the tallest walls seen so far from each side.
        left_max = 0
        right_max = 0

        trapped_water = 0

        # Process from both ends toward the center.
        # The side with the smaller current height is always safe to resolve,
        # because the opposite side already guarantees a boundary at least as high.
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    # A new left boundary raises the waterline for future positions.
                    left_max = height[left]
                else:
                    # Water above this bar is limited by the best left boundary so far.
                    trapped_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    # A new right boundary raises the waterline for future positions.
                    right_max = height[right]
                else:
                    # Water above this bar is limited by the best right boundary so far.
                    trapped_water += right_max - height[right]
                right -= 1

        return trapped_water