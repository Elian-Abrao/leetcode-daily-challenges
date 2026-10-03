class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        """
        Returns the k-th (1-indexed) character of the fully decoded string.
        Works backwards using the total length to avoid constructing the string.
        """
        # 1. Compute total decoded length from the encoded string.
        total_len = 0
        for ch in s:
            if ch.isdigit():
                total_len *= int(ch)          # repeat the current tape d times
            else:
                total_len += 1                 # add one letter

        # 2. Walk backwards from the end to locate the k-th character.
        #    total_len always reflects the current segment's decoded length.
        for ch in reversed(s):
            # Reduce k modulo the current block size.
            # This mirrors the effect of unwinding one repetition.
            k %= total_len
            if k == 0:
                k = total_len

            if ch.isalpha():
                # If k matches the position of this letter, it's our answer.
                if k == total_len:
                    return ch
                # Otherwise, this letter is not the target; remove it.
                total_len -= 1
            else:
                # Digit: the tape before this digit had length total_len // d.
                # Undo the repetition by dividing the length.
                total_len //= int(ch)
                # k already adjusted above; continue to previous character.

        # The problem guarantees a solution, so we never reach here.
        return ""