from __future__ import annotations
from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        """
        Build a permutation of [0, n] that satisfies the I/D pattern.
        Strategy: use two pointers (low and high) and assign greedily.
        - When we see 'I', we need perm[i] < perm[i+1], so place the current smallest
          remaining number (low) to make room for larger numbers later.
        - When we see 'D', we need perm[i] > perm[i+1], so place the current largest
          remaining number (high) to allow smaller numbers later.
        - After processing the n characters, one number remains; append it.
        
        Time: O(n), Space: O(n) for output (not counting output is O(1)).
        """
        n = len(s)
        low = 0          # smallest unused number
        high = n         # largest unused number
        perm = [0] * (n + 1)  # pre-allocate output for efficiency
        
        for i, ch in enumerate(s):
            if ch == 'I':
                perm[i] = low
                low += 1
            else:  # ch == 'D'
                perm[i] = high
                high -= 1
        
        # Last position gets the only remaining number (low == high at this point)
        perm[n] = low
        return perm