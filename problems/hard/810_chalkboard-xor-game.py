from typing import List
from functools import reduce
from operator import xor

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        # Calculate XOR of all elements
        total_xor = reduce(xor, nums, 0)
        
        # Alice wins immediately if XOR is already 0
        if total_xor == 0:
            return True
        
        # If XOR is non-zero and array length is even, Alice wins
        # Reasoning: With even count and non-zero XOR, Alice can always
        # find a move that doesn't make XOR = 0 (by pigeonhole principle).
        # If all moves led to XOR = 0, all elements would be identical to total_xor,
        # but then XOR of even count of identical elements would be 0 (contradiction).
        # So Alice can keep playing safely, and Bob will eventually face
        # an odd-length array with non-zero XOR where he must lose.
        if len(nums) % 2 == 0:
            return True
        
        # Alice loses: odd length with non-zero XOR
        # No guaranteed safe move exists for Alice
        return False