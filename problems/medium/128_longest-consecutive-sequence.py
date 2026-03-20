from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Empty input has no sequence.
        if not nums:
            return 0

        # Deduplicate first; this keeps the algorithm linear and avoids
        # reprocessing the same value many times.
        values = set(nums)
        longest = 0

        for value in values:
            # Only start counting from the beginning of a sequence.
            # If value - 1 exists, this value belongs to a sequence
            # that will be counted from an earlier number.
            if value - 1 in values:
                continue

            current = value
            length = 1

            # Expand forward while numbers stay consecutive.
            # Across all starts, each number is visited at most once here.
            while current + 1 in values:
                current += 1
                length += 1

            # Track the best sequence seen so far.
            if length > longest:
                longest = length

        return longest