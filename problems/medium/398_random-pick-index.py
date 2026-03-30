from typing import List
import random


class Solution:
    def __init__(self, nums: List[int]):
        # Precompute all positions for each value so every pick is O(1).
        # This uses extra memory, but it is fully acceptable for the constraints
        # and avoids scanning the array on every query.
        self.indices_by_value = {}

        for index, value in enumerate(nums):
            if value not in self.indices_by_value:
                self.indices_by_value[value] = []
            self.indices_by_value[value].append(index)

    def pick(self, target: int) -> int:
        # The problem guarantees target exists, so the lookup is always valid.
        indices = self.indices_by_value[target]

        # Uniformly choose one stored index.
        # random.choice gives each occurrence the same probability.
        return random.choice(indices)