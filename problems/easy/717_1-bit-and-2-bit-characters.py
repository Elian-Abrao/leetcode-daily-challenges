class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n = len(bits)
        i = 0

        # Greedily decode from left to right.
        # A '1' must start a two-bit character, so skip two bits.
        # A '0' must be a one-bit character, so move one bit.
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        # If decoding stops exactly at the last bit, that bit is a
        # one-bit character. Otherwise, it was consumed as a second bit.
        return i == n - 1