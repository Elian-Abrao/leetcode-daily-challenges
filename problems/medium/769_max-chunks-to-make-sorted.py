from __future__ import annotations

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        """
        Returns the maximum number of chunks to partition arr (a permutation of 0..n-1)
        such that sorting each chunk individually yields the sorted array.
        """
        chunks = 0
        max_seen = 0  # maximum value encountered so far in the current prefix

        for i, num in enumerate(arr):
            # Update the maximum in the prefix ending at i.
            max_seen = max(max_seen, num)
            # If the maximum equals the current index, then the prefix [0..i]
            # contains exactly the numbers 0..i, so we can end a chunk here.
            if max_seen == i:
                chunks += 1

        return chunks