from __future__ import annotations
from typing import List

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        # We only need to consider bits up to 30 (since values <= 1e9 < 2^30)
        MAXB = 31
        # par1[b] will be 1 if the count of numbers in arr1 with bit b set is odd, else 0
        par1 = [0] * MAXB
        # par2[b] similarly for arr2
        par2 = [0] * MAXB

        # Compute parity of each bit across arr1
        for x in arr1:
            b = 0
            while x:
                if x & 1:
                    par1[b] ^= 1  # flip parity if this bit is 1 in x
                x >>= 1
                b += 1

        # Compute parity of each bit across arr2
        for y in arr2:
            b = 0
            while y:
                if y & 1:
                    par2[b] ^= 1
                y >>= 1
                b += 1

        # The XOR sum across all pairwise ANDs:
        # For bit b, the total number of pairs with that bit set is (count1_b * count2_b).
        # This is odd iff both parities are 1. So set bit b in result iff par1[b] & par2[b] == 1.
        res = 0
        for b in range(MAXB):
            if par1[b] & par2[b]:
                res |= (1 << b)

        return res