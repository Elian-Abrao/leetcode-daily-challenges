from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # The doctor limits Alice to exactly half of all candies.
        max_candies_eaten = len(candyType) // 2

        # Distinct candy types represent the maximum variety she could possibly try.
        unique_types = len(set(candyType))

        # She cannot eat more unique types than the number of candies allowed.
        return min(max_candies_eaten, unique_types)