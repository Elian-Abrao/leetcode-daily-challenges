class Solution:
    def binaryGap(self, n: int) -> int:
        # Track the position of the most recent 1 bit.
        last = -1
        ans = 0
        pos = 0

        while n:
            if n & 1:  # current bit is 1
                if last != -1:
                    # This is the next set bit, so they are adjacent in terms of 1's.
                    ans = max(ans, pos - last)
                last = pos
            n >>= 1
            pos += 1

        return ans