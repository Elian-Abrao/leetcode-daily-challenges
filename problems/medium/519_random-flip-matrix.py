import random
from typing import List

class Solution:

    def __init__(self, m: int, n: int):
        """
        Initialize with m rows and n columns.
        total = m * n is the number of cells.
        We maintain a virtual array of indices 0..total-1.
        As we flip cells, we swap the chosen index with the last remaining index,
        tracking only those indices that have been involved in a swap.
        """
        self.m = m
        self.n = n
        self.total = m * n          # total number of cells
        self.remaining = self.total  # number of cells still zero
        self.map = {}               # virtual index -> actual index (if swapped)

    def flip(self) -> List[int]:
        """
        Randomly pick a zero cell, flip it to 1, and return its coordinates [i, j].
        Uses Fisher-Yates style sampling in O(1) amortized time.
        """
        # Pick a random position among the remaining cells
        rand = random.randrange(0, self.remaining)

        # The actual index stored at this virtual position
        idx = self.map.get(rand, rand)

        # Compute row and column from the flat index
        i = idx // self.n
        j = idx % self.n

        # Reduce the pool size (remove the chosen cell)
        self.remaining -= 1

        # Swap the chosen position with the last position in the virtual array
        last = self.remaining  # this is the index of the last element before decrement
        if rand != last:
            # Value that currently resides at the last position
            last_val = self.map.get(last, last)
            # After swap, the chosen position gets that value
            self.map[rand] = last_val
            # The last position (now out of the pool) can be forgotten.
            # No need to delete its mapping; it will never be accessed again.

        return [i, j]

    def reset(self) -> None:
        """
        Reset all cells to 0. Simply restore initial state.
        """
        self.remaining = self.total
        self.map.clear()