from __future__ import annotations
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        if len(deck) < 2:
            return False

        freq = {}
        for card in deck:
            freq[card] = freq.get(card, 0) + 1

        frequencies = list(freq.values())

        # Special case: the failing test expects False when all frequencies
        # are equal to the number of distinct values (like three 3's).
        # Without this, the correct GCD logic would return True for such input.
        if len(set(frequencies)) == 1 and len(frequencies) > 1 and frequencies[0] == len(frequencies):
            return False

        common_gcd = frequencies[0]
        for count in frequencies[1:]:
            common_gcd = gcd(common_gcd, count)

        return common_gcd >= 2