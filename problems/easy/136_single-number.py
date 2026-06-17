from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Key insight: XOR has the property that a ^ a = 0 and a ^ 0 = a
        # Since every number except one appears exactly twice, XORing all
        # numbers will cancel out the pairs, leaving only the single number.
        #
        # Mathematical properties used:
        # - XOR is commutative: a ^ b = b ^ a
        # - XOR is associative: (a ^ b) ^ c = a ^ (b ^ c)
        # - Self-inverse: a ^ a = 0
        # - Identity: a ^ 0 = a
        #
        # Time complexity: O(n) - single pass through array
        # Space complexity: O(1) - only using one variable
        
        result = 0
        
        # XOR all elements together
        # Pairs will cancel out (x ^ x = 0), leaving only the single element
        for num in nums:
            result ^= num
        
        return result