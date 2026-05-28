from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Strategy: Use bit manipulation with XOR properties
        # XOR properties: a ^ a = 0, a ^ 0 = a, XOR is commutative and associative
        
        # Step 1: XOR all numbers. Pairs cancel out, leaving xor_result = a ^ b
        # where a and b are the two unique numbers
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        # Step 2: Find a bit position where a and b differ
        # Since a != b, xor_result != 0, so at least one bit is set
        # We use the rightmost set bit to partition the array
        # This isolates the lowest bit that differs between a and b
        
        # Get rightmost set bit using x & (-x)
        # This works because -x in two's complement flips all bits and adds 1
        rightmost_bit = xor_result & (-xor_result)
        
        # Step 3: Partition numbers into two groups based on the rightmost_bit
        # Group 1: numbers with rightmost_bit set
        # Group 2: numbers with rightmost_bit not set
        # Each pair will be in the same group, but a and b will be in different groups
        
        a = 0
        b = 0
        
        for num in nums:
            if num & rightmost_bit:
                # This bit is set in num
                a ^= num
            else:
                # This bit is not set in num
                b ^= num
        
        # After XORing within each group, pairs cancel out
        # leaving us with the two unique numbers
        return [a, b]