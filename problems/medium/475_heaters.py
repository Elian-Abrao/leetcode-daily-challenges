from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Handle edge cases gracefully (though constraints ensure non-empty inputs)
        if not houses or not heaters:
            return 0

        # Sort both arrays to enable linear-time merge-like processing
        houses.sort()
        heaters.sort()

        i = 0  # Pointer to the first heater at or to the right of the current house
        max_radius = 0

        for h in houses:
            # Move the heater pointer to the position where heaters[i] >= h, if possible
            while i < len(heaters) and heaters[i] < h:
                i += 1

            # Distances to the nearest heater on the left and on the right (if they exist)
            left_dist = float('inf')
            right_dist = float('inf')

            if i > 0:
                left_dist = h - heaters[i - 1]        # Nearest heater to the left
            if i < len(heaters):
                right_dist = heaters[i] - h           # Nearest heater to the right

            dist = min(left_dist, right_dist)        # Closest heater distance for this house
            if dist > max_radius:
                max_radius = dist

        return max_radius