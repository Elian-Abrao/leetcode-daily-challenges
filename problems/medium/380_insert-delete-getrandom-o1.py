from __future__ import annotations
import random

class Solution:
    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        idx_to_remove = self.val_to_index[val]
        last_val = self.values[-1]

        self.values[idx_to_remove] = last_val
        self.val_to_index[last_val] = idx_to_remove

        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)