class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Negative numbers and zero are not powers of four
        if n <= 0:
            return False
        # A power of four has exactly one bit set (is a power of two)
        if (n & (n - 1)) != 0:
            return False
        # The single set bit must be at an even index (0-based).
        # 0x55555555 has 1s at all even bit positions in 32-bit representation.
        return (n & 0x55555555) != 0