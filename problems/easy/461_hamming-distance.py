class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR gives 1 wherever bits differ, 0 where they match
        # Then count the number of 1s in the XOR result
        xor_result = x ^ y
        
        # Count set bits (1s) in xor_result
        # Use Brian Kernighan's algorithm: n & (n-1) clears the lowest set bit
        count = 0
        while xor_result:
            xor_result &= xor_result - 1  # Clear the lowest set bit
            count += 1
        
        return count