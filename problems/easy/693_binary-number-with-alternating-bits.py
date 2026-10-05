class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # If adjacent bits always differ, then n and n >> 1 differ at every bit
        # that exists in n. Thus n ^ (n >> 1) produces a string of all 1s.
        x = n ^ (n >> 1)

        # A positive number consisting entirely of 1s has the form 2^k - 1.
        # For such numbers, x & (x + 1) == 0.
        # Example: x = 7 (111), x + 1 = 8 (1000), 7 & 8 == 0.
        return (x & (x + 1)) == 0