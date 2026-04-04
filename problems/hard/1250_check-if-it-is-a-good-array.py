from typing import List
from math import gcd


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # By Bezout's identity, all integer linear combinations of nums
        # are exactly the multiples of gcd(nums). So we can make 1 iff gcd is 1.
        current_gcd = 0

        for value in nums:
            current_gcd = gcd(current_gcd, value)

            # Early exit: once gcd becomes 1, no later value can improve it further.
            if current_gcd == 1:
                return True

        # If we never reached 1, every achievable sum is a multiple of gcd > 1.
        return False