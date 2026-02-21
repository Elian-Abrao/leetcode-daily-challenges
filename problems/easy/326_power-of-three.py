class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Powers of three are positive; immediately reject non-positive numbers.
        if n <= 0:
            return False

        # The largest power of 3 within 32-bit signed int is 3^19 = 1162261467.
        # If n is a power of three, it must be a divisor of 3^19.
        max_power_three_32bit = 1162261467  # 3^19

        # If max_power_three_32bit is divisible by n, then n is a power of three.
        return max_power_three_32bit % n == 0