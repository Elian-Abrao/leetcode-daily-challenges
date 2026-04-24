from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        """
        Determine the minimum number of k-length flips needed to make all bits 1.
        We sweep left-to-right while tracking how many flips are currently
        affecting the current position (parity). We use a simple array
        'flipped' to record when a flip started, so its effect ends after
        exactly k elements.
        """
        n = len(nums)
        if n == 0:
            return 0

        # flipped[i] == 1 means a flip started at index i
        flipped = [0] * n

        parity = 0  # current number of flips affecting index i, modulo 2
        ans = 0

        for i in range(n):
            # If a flip started at i - k goes out of the window, reduce parity
            if i >= k and flipped[i - k]:
                parity ^= 1
                flipped[i - k] = 0  # clear to keep memory clean

            # Current effective bit after applying all active flips
            current = nums[i] ^ parity

            if current == 0:
                # Need to flip window starting at i
                if i + k > n:
                    return -1  # insufficient space to place a window
                ans += 1
                parity ^= 1
                flipped[i] = 1  # mark that a flip starts here

        return ans