class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # XOR cancels equal characters regardless of order:
        # a ^ a = 0, so only the extra character remains.
        xor_value = 0

        # Process both strings; duplicates are handled naturally by XOR.
        for ch in s:
            xor_value ^= ord(ch)

        # t has exactly one additional character, so its code point survives.
        for ch in t:
            xor_value ^= ord(ch)

        # Constraints guarantee there is one valid answer.
        return chr(xor_value)