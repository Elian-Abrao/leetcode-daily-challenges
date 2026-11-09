from __future__ import annotations
from typing import List, Tuple

class MyHashMap:
    """
    A simple hash map implementation with separate chaining.
    The bucket count is chosen as a prime (~10 007) to distribute keys evenly.
    With at most 10^4 calls, each bucket will hold on average 1 element,
    yielding amortized O(1) time for all operations.
    """

    def __init__(self) -> None:
        # Choose a prime number of buckets for better distribution.
        self._capacity: int = 10007
        # Each bucket is a list of (key, value) pairs.
        self._table: List[List[Tuple[int, int]]] = [[] for _ in range(self._capacity)]

    def _hash(self, key: int) -> int:
        """Return the bucket index for a given key."""
        return key % self._capacity

    def put(self, key: int, value: int) -> None:
        """Insert (key, value) or update if key already exists."""
        idx = self._hash(key)
        bucket = self._table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Key found → update value.
                bucket[i] = (key, value)
                return
        # Key not found → append new pair.
        bucket.append((key, value))

    def get(self, key: int) -> int:
        """Return the value for key, or -1 if key is not present."""
        idx = self._hash(key)
        bucket = self._table[idx]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """Remove the mapping for key if it exists."""
        idx = self._hash(key)
        bucket = self._table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Remove the (key, value) pair by index.
                bucket.pop(i)
                return