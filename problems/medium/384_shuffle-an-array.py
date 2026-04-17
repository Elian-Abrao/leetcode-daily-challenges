import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        # Store the original configuration for reset and a working copy for shuffle
        self._original = nums[:]
        self._array = nums[:]

    def reset(self) -> List[int]:
        # Reset to the original configuration and return it
        self._array = self._original[:]
        return self._array

    def shuffle(self) -> List[int]:
        # In-place Fisher-Yates shuffle on the working array to ensure uniform randomness
        arr = self._array
        n = len(arr)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr