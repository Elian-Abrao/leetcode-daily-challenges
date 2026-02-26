class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Positive numbers with exactly one bit set in binary representation are powers of two.
        # n > 0 ensures we exclude zero and negatives; (n & (n - 1)) == 0 checks the single-set-bit property.
        if n <= 0:
            return False
        return (n & (n - 1)) == 0