from typing import List
import random

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        # Core idea: Map blacklisted numbers in [0, M) to valid numbers in [M, n)
        # where M = n - len(blacklist) is the count of valid numbers.
        # After mapping, we can pick uniformly from [0, M) and use the mapping.
        
        self.M = n - len(blacklist)  # Number of valid integers
        self.mapping = {}  # Maps blacklisted integers in [0, M) to valid ones in [M, n)
        
        # Convert blacklist to a set for O(1) lookup
        blacklist_set = set(blacklist)
        
        # Find all valid numbers in the range [M, n) that are not blacklisted
        # These will be used as replacement values for blacklisted numbers in [0, M)
        valid_in_upper_range = []
        for num in range(self.M, n):
            if num not in blacklist_set:
                valid_in_upper_range.append(num)
        
        # Map each blacklisted number in [0, M) to a valid number in [M, n)
        # Blacklisted numbers in [M, n) don't need mapping since we never pick them
        idx = 0
        for b in blacklist:
            if b < self.M:
                # This blacklisted number is in the picking range, so remap it
                self.mapping[b] = valid_in_upper_range[idx]
                idx += 1

    def pick(self) -> int:
        # Pick a random index in [0, M)
        rand_idx = random.randint(0, self.M - 1)
        
        # If this index is blacklisted, return its mapped value
        # Otherwise, return the index itself
        return self.mapping.get(rand_idx, rand_idx)