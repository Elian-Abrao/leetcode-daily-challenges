class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Compute the sum of two integers without using '+' or '-'.
        Uses bitwise operations with 32-bit masking to emulate two's complement addition.
        """
        MASK = 0xFFFFFFFF       # Mask to keep values within 32 bits
        MAX_INT = 0x7FFFFFFF    # Maximum positive int for 32-bit signed

        while b != 0:
            # carry contains bits that need to be added in the next higher position
            carry = (a & b) << 1
            # sum without carry, restricted to 32 bits
            a = (a ^ b) & MASK
            # prepare next round with the carry
            b = carry & MASK

        # If a represents a negative number in 32-bit, convert back to Python int
        return a if a <= MAX_INT else a - (MASK + 1)