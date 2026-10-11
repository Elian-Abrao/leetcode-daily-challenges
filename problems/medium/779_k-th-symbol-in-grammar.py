class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # The first row is always 0.
        # Each row is the previous row followed by its bitwise inverse.
        # Moving from row n down to row 1, every time we go into the
        # second half, the symbol is inverted relative to the first half.
        result = 0

        while n > 1:
            # Length of the previous row = half the length of the current row.
            mid = 1 << (n - 2)  # 2^(n-2)

            if k > mid:
                # We are in the inverted second half.
                result = 1 - result
                k -= mid  # Map to the corresponding position in the first half.

            n -= 1

        return result