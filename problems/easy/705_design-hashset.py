from __future__ import annotations

class Solution:
    def __init__(self):
        self._storage = bytearray(1_000_001)

    def add(self, key: int) -> None:
        self._storage[key] = 1

    def remove(self, key: int) -> None:
        self._storage[key] = 0

    def contains(self, key: int) -> bool:
        return self._storage[key] == 1